from django.urls import path

# from products.views import add_to_cart
from .views import *

app_name = 'orders'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    # path('get_size/<slug:slug>', get_product_variation_size, name='get-size'),
    path('add_to_cart/<slug:slug>', add_to_cart, name='add-to-cart'),
]
