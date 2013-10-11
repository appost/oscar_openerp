import oscar
from datetime import datetime
from oscar.core.utils import slugify
from oscar.apps.dashboard.catalogue.forms import CategoryForm
from django.db.models import get_model


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

def sort_ids(oe_vals):
    ids = []
    for i in range(0, len(oe_vals)):
        ids.append(oe_vals[i]['id'])
    ids.sort()
    return ids

def get_index(seq, attr, value):
    return next(index for (index, d) in enumerate(seq) if d[attr] == value)

def oe_val_by_id(oe_val, id):
    index = get_index(oe_val, 'id', id)
    return oe_val[index]


def imp_product_template(client):
    oe_mod_name = 'product.template'
    oe_mod_fieds = ['type']
    oe_mod_val = get_oe_mod_val(client, oe_mod_name, oe_mod_fieds)
    oscar_mod = oscar.apps.catalogue.models.ProductClass
    for i in range(0, len(oe_mod_val)):
        oscar_mod_obj = oscar_mod(id = i)
        oscar_mod_obj.name = oe_mod_val[i]['type']
        oscar_mod_obj.slug = slugify(oe_mod_val[i]['type'])
        oscar_mod_obj.save()

def imp_product_category(client):
    oe_mod_name = 'product.category'
    oe_mod_fieds = ['id', 'name', 'parent_id']
    oe_mod_val = get_oe_mod_val(client, oe_mod_name, oe_mod_fieds)
    oscar_mod = oscar.apps.catalogue.models.Category
    for i in sort_ids(oe_mod_val):
        oscar_mod_obj = oscar_mod(id = i)
        oe_mod_val_cur = oe_val_by_id(oe_mod_val, i)
        if oe_mod_val_cur['parent_id'] == False:
            oscar.apps.catalogue.models.Category.add_root(id = i, name = oe_mod_val_cur['name'])
        else:
            oscar_mod_obj_prnt = oscar.apps.catalogue.models.Category.objects.get(id = oe_mod_val_cur['parent_id'][0])
            oscar_mod_obj_prnt.add_child(id = i, name = oe_mod_val_cur['name'])

def imp_res_partner(client):
    oe_mod_name = 'res.partner'
    oe_mod_fieds = ['id', 'name']
    oe_mod_val = get_oe_mod_val(client, oe_mod_name, oe_mod_fieds)
    oscar_mod = oscar.apps.partner.models.Partner
    for i in sort_ids(oe_mod_val):
        oscar_mod_obj = oscar_mod(id = i)
        oe_mod_val_cur = oe_val_by_id(oe_mod_val, i)
        oscar_mod_obj.name = oe_mod_val_cur['name']
        oscar_mod_obj.save()
    

            
def imp_product_product(client):
    oe_mod_name = 'product.product'
    ########################################42#
    #mod_val = client.read(oe_mod_name,[])
    #get_index(mod_val, 'name', 'name_product')
    #########################################
    oe_mod_fieds = ['id', 'name','code','type','description','categ_id']
    oe_mod_val = get_oe_mod_val(client, oe_mod_name, oe_mod_fieds)
    #oscar_mod = oscar.apps.catalogue.models.Product
    oscar_mod = get_model('catalogue', 'product')
    for i in sort_ids(oe_mod_val):
        oscar_mod_obj = oscar_mod(id = i)
        oe_mod_val_cur = oe_val_by_id(oe_mod_val, i)
        oscar_mod_obj.title = oe_mod_val_cur['name']
        if oe_mod_val_cur['code']:
            oscar_mod_obj.upc = oe_mod_val_cur['code']
        prodclass = oscar.apps.catalogue.models.ProductClass.objects.get(name=oe_mod_val_cur['type'])
        oscar_mod_obj.product_class_id = prodclass.id
        oscar_mod_obj.description = oe_mod_val_cur['description']
        category = oscar.apps.catalogue.models.Category.objects.get(id=oe_mod_val_cur['categ_id'][0])
        productcategory = oscar.apps.catalogue.models.ProductCategory.objects.get_or_create(category = category, product = oscar_mod_obj)[0]
        oscar_mod_obj.productcategory_set.add(productcategory)
        #import ipdb; ipdb.set_trace()
        oscar_mod_obj.date_created = datetime.now()
        oscar_mod_obj.save()


def imp_product_product(client):
    oe_mod_name = 'product.product'
    ########################################42#
    #mod_val = client.read(oe_mod_name,[])
    #get_index(mod_val, 'name', 'name_product')
    #########################################
    oe_mod_fieds = ['id', 'name','code','type','description','categ_id']
    oe_mod_val = get_oe_mod_val(client, oe_mod_name, oe_mod_fieds)
    #oscar_mod = oscar.apps.catalogue.models.Product
    oscar_mod = get_model('catalogue', 'product')
    for i in sort_ids(oe_mod_val):
        oscar_mod_obj = oscar_mod(id = i)
        oe_mod_val_cur = oe_val_by_id(oe_mod_val, i)
        oscar_mod_obj.title = oe_mod_val_cur['name']
        if oe_mod_val_cur['code']:
            oscar_mod_obj.upc = oe_mod_val_cur['code']
        prodclass = oscar.apps.catalogue.models.ProductClass.objects.get(name=oe_mod_val_cur['type'])
        oscar_mod_obj.product_class_id = prodclass.id
        oscar_mod_obj.description = oe_mod_val_cur['description']
        category = oscar.apps.catalogue.models.Category.objects.get(id=oe_mod_val_cur['categ_id'][0])
        productcategory = oscar.apps.catalogue.models.ProductCategory.objects.get_or_create(category = category, product = oscar_mod_obj)[0]
        oscar_mod_obj.productcategory_set.add(productcategory)
        #import ipdb; ipdb.set_trace()
        oscar_mod_obj.date_created = datetime.now()
        oscar_mod_obj.save()

