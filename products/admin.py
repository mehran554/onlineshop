from django.contrib import admin
from .models import Product


class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'price', 'datetime_created', 'active']


admin.site.register(Product, AdminProduct)
