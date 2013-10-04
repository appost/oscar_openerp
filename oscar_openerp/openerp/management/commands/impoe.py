from django.core.management.base import NoArgsCommand, make_option
import erppeek
import os
import sys
#from os.environ.setdefault("DJANGO_SETTINGS_MODULE", "esale.settings")

from oscar_openerp import settings
from django.db import models
from oscar.apps.catalogue.models import ProductClass
from oscar_openerp.openerp import mapping 
import oscar

def distinct(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]


def distinct_dict(seq):
    seen = set()
    new_seq = []
    for d in seq:
        t = tuple(sorted(d.items()))
        if t not in seen:
            seen.add(t)
            new_seq.append(d)
    return new_seq


class Command(NoArgsCommand):

    help = "Whatever you want to print here"

    option_list = NoArgsCommand.option_list + (
        make_option('--verbose', action='store_true'),
    )

    def handle_noargs(self, **options):
        cate = models.get_model('catalogue', 'Category')
        Client = erppeek.Client(
            settings.OSCAR_ERP_SERVER,
            db=settings.OSCAR_ERP_DATABASE,
            user=settings.OSCAR_ERP_USERNAME,
            password=settings.OSCAR_ERP_PASSWORD
            )
        oecate = Client.read("product.template",[],'type')
        oecate = distinct(oecate)
        for i in range(0, len(oecate)):
            productclass = ProductClass(id=i,name=oecate[i],slug=oecate[i])
            productclass.save()
        for oe_mod_name in mapping.mapping:   
            oe_mod_val = Client.read(oe_mod_name,[],mapping.mapping[oe_mod_name][1].keys())
            if 'id' not in mapping.mapping[oe_mod_name][1].keys():
                for dict in oe_mod_val:
                    del dict['id']
                oe_mod_val = distinct_dict(oe_mod_val)
            oscar_mod = eval(mapping.mapping[oe_mod_name][0])
            for i in range(0, len(oe_mod_val)):
                oscar_mod_obj = oscar_mod(id = i)
                for oe_field in oe_mod_val[i].keys():
                    oeattr=oe_mod_val[i][oe_field]
                    for attr in mapping.mapping[oe_mod_name][1][oe_field]:
                        setattr(oscar_mod_obj, attr, oeattr)
                #import ipdb; ipdb.set_trace()
                oscar_mod_obj.save()
        
        














