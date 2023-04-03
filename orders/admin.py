from django.contrib import admin

from .models import Order, OrderItem
from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price']
    extra = 1


# @admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    # fields = ['user', 'first_name', 'last_name','is_paid']
    list_display = ['user', 'first_name', 'last_name', 'datetime_created', 'is_paid', ]
    inlines = [OrderItemInline, ]


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    List_display = ['order', 'product', 'quantity', 'price']


admin.site.register(OrderItem, OrderItemAdmin)
