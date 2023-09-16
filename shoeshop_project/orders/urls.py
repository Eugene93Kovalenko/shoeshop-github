from django.urls import path

# from products.views import add_to_cart
from .views import *

app_name = 'orders'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<slug:slug>', add_to_cart, name='add-to-cart'),
]
