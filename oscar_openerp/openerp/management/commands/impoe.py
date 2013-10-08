from django.core.management.base import NoArgsCommand, make_option
import erppeek

from oscar_openerp import settings
from oscar_openerp.openerp import mapping 
import oscar

def distinct_dict(seq):
    seen = set()
    new_seq = []
    for d in seq:
        t = tuple(sorted(d.items()))
        if t not in seen:
            seen.add(t)
            new_seq.append(d)
    return new_seq

def get_oe_mod_val(client, mod_name, fields):
    mod_val = client.read(mod_name,[],fields)
    if 'id' not in fields:
        for dict in mod_val:
            del dict['id']
        mod_val = distinct_dict(mod_val)
    return mod_val
    

class Command(NoArgsCommand):

    help = "Whatever you want to print here"

    option_list = NoArgsCommand.option_list + (
        make_option('--verbose', action='store_true'),
    )

    def handle_noargs(self, **options):
        Client = erppeek.Client(
            settings.OSCAR_ERP_SERVER,
            db=settings.OSCAR_ERP_DATABASE,
            user=settings.OSCAR_ERP_USERNAME,
            password=settings.OSCAR_ERP_PASSWORD
            )
        import ipdb; ipdb.set_trace()
        for oe_mod_name in mapping.mapping:
            oe_mod_fieds = mapping.mapping[oe_mod_name][1].keys()
            oe_mod_val = get_oe_mod_val(Client, oe_mod_name, oe_mod_fieds)
            import ipdb; ipdb.set_trace()
            oscar_mod = eval(mapping.mapping[oe_mod_name][0])
            for i in range(0, len(oe_mod_val)):
                oscar_mod_obj = oscar_mod(id = i)
                for oe_field in oe_mod_val[i].keys():
                    oeattr=oe_mod_val[i][oe_field]
                    for attr in mapping.mapping[oe_mod_name][1][oe_field]:
                        setattr(oscar_mod_obj, attr, oeattr)
                oscar_mod_obj.save()
        














