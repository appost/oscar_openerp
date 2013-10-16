import oe_data_migr

mapping_oscar = {
           'category' : {
                         'id' : 'id',
                         'name' : 'name'                         
                         }
           
           }
    boh = all_to_dict(oscar_mod.objects.all())


'''
mapping = {
           'product.template' : [
                                 'oscar.apps.catalogue.models.ProductClass', \
                                        {
                                          'type' : ['name', 'slug'] #vedere slugify
                                          }           
                                 ],
           'product.category' : [
                                 'oscar.apps.catalogue.models.Category', \
                                        {
                                          'type' : ['name', 'slug'] 
                                          }           
                                 ],
           }
           
'''