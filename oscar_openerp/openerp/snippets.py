import erppeek
#import settings



Client = erppeek.Client(
    settings.OSCAR_ERP_SERVER,
    db=settings.OSCAR_ERP_DATABASE,
    user=settings.OSCAR_ERP_USERNAME,
    password=settings.OSCAR_ERP_PASSWORD
    )
oecate = Client.read("product.template")
