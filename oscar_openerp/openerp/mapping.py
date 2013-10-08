import oe_data_migr
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