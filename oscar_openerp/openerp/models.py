# from django.db import models
# 
# class ResUsers(models.Model):
#     id = models.IntegerField(primary_key=True)
#     active = models.BooleanField(blank=True)
#     login = models.CharField(max_length=64, unique=True)
#     password = models.CharField(max_length=64, blank=True)
#     create_date = models.DateTimeField(null=True, blank=True)
#     write_date = models.DateTimeField(null=True, blank=True)
#     menu_id = models.IntegerField(null=True, blank=True)
#     login_date = models.DateField(null=True, blank=True)
#     signature = models.TextField(blank=True)
#     action_id = models.IntegerField(null=True, blank=True)
#     share = models.BooleanField(blank=True)
#     class Meta:
#         db_table = u'res_users'
# 
# class ProductUomCateg(models.Model):
#     id = models.IntegerField(primary_key=True)
#     create_uid = models.ForeignKey(ResUsers, null=True, db_column='create_uid', blank=True)
#     create_date = models.DateTimeField(null=True, blank=True)
#     write_date = models.DateTimeField(null=True, blank=True)
#     write_uid = models.ForeignKey(ResUsers, null=True, db_column='write_uid', blank=True)
#     name = models.CharField(max_length=64)
#     class Meta:
#         db_table = u'product_uom_categ'
# 
# 
# class ProductUom(models.Model):
#     id = models.IntegerField(primary_key=True)
#     create_uid = models.ForeignKey(ResUsers, null=True, db_column='create_uid', blank=True)
#     create_date = models.DateTimeField(null=True, blank=True)
#     write_date = models.DateTimeField(null=True, blank=True)
#     write_uid = models.ForeignKey(ResUsers, null=True, db_column='write_uid', blank=True)
#     uom_type = models.CharField(max_length=-1)
#     category = models.ForeignKey(ProductUomCateg)
#     name = models.CharField(max_length=64)
#     rounding = models.DecimalField(max_digits=65535, decimal_places=65535)
#     factor = models.DecimalField(max_digits=65535, decimal_places=65535)
#     active = models.BooleanField(null=True, blank=True)
#     class Meta:
#         db_table = u'product_uom'
# 
# class ProductCategory(models.Model):
#     id = models.IntegerField(primary_key=True)
#     parent_left = models.IntegerField(null=True, blank=True)
#     parent_right = models.IntegerField(null=True, blank=True)
#     create_uid = models.ForeignKey(ResUsers, null=True, db_column='create_uid', blank=True)
#     create_date = models.DateTimeField(null=True, blank=True)
#     write_date = models.DateTimeField(null=True, blank=True)
#     write_uid = models.ForeignKey(ResUsers, null=True, db_column='write_uid', blank=True)
#     name = models.CharField(max_length=64)
#     sequence = models.IntegerField(null=True, blank=True)
#     parent = models.ForeignKey('self', null=True, blank=True)
#     type = models.CharField(max_length=-1, blank=True)
#     class Meta:
#         db_table = u'product_category'
# 
# class ResCompany(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=128, unique=True)
#     parent = models.ForeignKey('self', null=True, blank=True)
#     create_uid = models.ForeignKey(ResUsers, null=True, db_column='create_uid', blank=True)
#     create_date = models.DateTimeField(null=True, blank=True)
#     write_date = models.DateTimeField(null=True, blank=True)
#     write_uid = models.ForeignKey(ResUsers, null=True, db_column='write_uid', blank=True)
#     rml_footer = models.TextField(blank=True)
#     rml_header = models.TextField()
#     paper_format = models.CharField(max_length=-1)
#     logo_web = models.TextField(blank=True) # This field type is a guess.
#     rml_header2 = models.TextField()
#     rml_header3 = models.TextField()
#     rml_header1 = models.CharField(max_length=200, blank=True)
#     account_no = models.CharField(max_length=64, blank=True)
#     company_registry = models.CharField(max_length=64, blank=True)
#     custom_footer = models.BooleanField(null=True, blank=True)
#     expects_chart_of_accounts = models.BooleanField(null=True, blank=True)
#     paypal_account = models.CharField(max_length=128, blank=True)
#     overdue_msg = models.TextField(blank=True)
#     tax_calculation_rounding_method = models.CharField(max_length=-1, blank=True)
#     vat_check_vies = models.BooleanField(null=True, blank=True)
#     class Meta:
#         db_table = u'res_company'
# 
# 
# class ProductTemplate(models.Model):
#     id = models.IntegerField(primary_key=True)
#     create_uid = models.ForeignKey(ResUsers, null=True, db_column='create_uid', blank=True)
#     create_date = models.DateTimeField(null=True, blank=True)
#     write_date = models.DateTimeField(null=True, blank=True)
#     write_uid = models.ForeignKey(ResUsers, null=True, db_column='write_uid', blank=True)
#     warranty = models.FloatField(null=True, blank=True)
#     uos = models.ForeignKey(ProductUom, null=True, blank=True)
#     list_price = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
#     description = models.TextField(blank=True)
#     weight = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
#     weight_net = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
#     standard_price = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
#     mes_type = models.CharField(max_length=-1, blank=True)
#     uom = models.ForeignKey(ProductUom)
#     description_purchase = models.TextField(blank=True)
#     cost_method = models.CharField(max_length=-1)
#     categ = models.ForeignKey(ProductCategory)
#     name = models.CharField(max_length=128)
#     uos_coeff = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
#     volume = models.FloatField(null=True, blank=True)
#     sale_ok = models.BooleanField(null=True, blank=True)
#     description_sale = models.TextField(blank=True)
#     product_manager = models.ForeignKey(ResUsers, null=True, db_column='product_manager', blank=True)
#     company = models.ForeignKey(ResCompany, null=True, blank=True)
#     state = models.CharField(max_length=-1, blank=True)
#     produce_delay = models.FloatField(null=True, blank=True)
#     uom_po = models.ForeignKey(ProductUom)
#     rental = models.BooleanField(null=True, blank=True)
#     type = models.CharField(max_length=-1)
#     class Meta:
#         db_table = u'product_template'
