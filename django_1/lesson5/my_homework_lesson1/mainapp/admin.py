from django.contrib import admin
from mainapp.models import ProductCatalog, Main
from basketapp.models import Basket

# Register your models here.

admin.site.register(ProductCatalog)
admin.site.register(Main)
admin.site.register(Basket)
