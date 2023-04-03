from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext as _
from cart.cart import Cart
from .forms import OrderForm

from .models import OrderItem


def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
            messages.success(request, _("Successfully Process Register Your Order Cart"))
            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price
                )
            cart.clear()
    return render(request, 'orders/order_create.html', {'form': order_form})
