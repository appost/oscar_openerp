from django.core.management.base import NoArgsCommand, make_option
import erppeek

from oscar_openerp import settings
from oscar_openerp.openerp import oe_data_migr
import oscar


    

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
        oe_data_migr.imp_product_template(Client)
        oe_data_migr.imp_product_category(Client)
        oe_data_migr.imp_res_partner(Client)
        oe_data_migr.imp_product_product(Client)
        














