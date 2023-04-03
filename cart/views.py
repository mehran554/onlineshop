from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from django.contrib import messages
from products.models import Product
from cart.forms import FormAddProductToCart
from django.utils.translation import gettext as _
from django.views.decorators.http import require_POST


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    new_add_to_form = FormAddProductToCart(request.POST)
    if new_add_to_form.is_valid():
        cleaned_data = new_add_to_form.cleaned_data
        quantity = cleaned_data['quantity']
        replace_current_qty = cleaned_data['is_add']
        cart.add(product, quantity, replace_current_qty)
    # return redirect('cart:cart_detail')
    return redirect('product_list')


def cart_detail_view(request):
    cart = Cart(request)
    """
                 حال باید کاری کنیم که مقدار فیلد is_add  برابر True شود چون در صفحه جزییات کارت هستیم و آنجا بایستی هر مقداری واسه تعداد محصول درج شد همان مقدار نهایی دیتابیس باشد 
         """
    for item in cart:
        item['product_update_qty_form'] = FormAddProductToCart(initial={
            'quantity': item['quantity'],
            'is_add': True,
        }
        )
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def cart_remove_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    # if len(cart):
    #     return redirect('cart:cart_detail')
    # else:
    return redirect('product_list')


def cart_total_price(request):
    cart = Cart(request)
    # for item in cart:
    #     total_price=item.
    # cart['total_price']
    return cart.get_total_price()


@require_POST
def cart_clear_view(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.warning(request, _("Successfully Empty Your Cart"))
    else:
        messages.error(request, _("You Cart Is Already Empty!!!! "))
    return redirect('product_list')
# @require_POST
# def cart_clear_view(request):
#     cart = Cart(request)
#
#     if len(cart):
#         cart.clear()
#         messages.success(request, _('All products successfully removed from your cart'))
#     else:
#         messages.warning(request, _('Your cart is already empty'))
#
#     return redirect('product_list')
