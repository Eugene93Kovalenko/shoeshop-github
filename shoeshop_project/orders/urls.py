from django.urls import path

from .views import *

app_name = 'orders'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<slug:slug>', add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<slug:slug>', remove_from_cart, name='remove-from-cart'),
]
