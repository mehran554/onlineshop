from django.db import models
from django.conf import settings
from products.models import Product
from django.utils.translation import gettext as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Username'))
    first_name = models.CharField(_('Name'), max_length=100)
    last_name = models.CharField(_('LastName'), max_length=100)
    phone_number = models.CharField(_('PhoneNumber'), max_length=15)
    address = models.CharField(_('Address'), max_length=700)
    order_note = models.CharField(_('Order_Note'), max_length=700, blank=True)
    zibal_trackId = models.CharField(max_length=255, blank=True)
    zibal_refNumber = models.CharField(max_length=150, blank=True)
    zibal_data = models.TextField(blank=True)
    is_paid = models.BooleanField(_('Is_Paid'), default=False)
    datetime_created = models.DateTimeField(_('DateTime_Create'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('DateTime_Modified'), auto_now=True)

    # email=models.EmailField()

    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())
        # result = 0
        # for item in self.items.all():
        #     result += item.price * item.quantity
        # return result

    def __str__(self):
        return f'order:{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'order item {self.id}: {self.product} x {self.quantity} (price:{self.price}) '
