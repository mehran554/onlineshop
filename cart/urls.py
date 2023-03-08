from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('clear/', views.cart_clear_view, name='cart_clear'),
    path('add/<int:product_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('remove/<int:product_id>/', views.cart_remove_view, name='cart_remove'),
    # path('total/<int:product_id>/', views.cart_remove_view, name='cart_remove'),

]
