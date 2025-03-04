from django.contrib import admin
from payments.models import Product

class ProductsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductsAdmin)
