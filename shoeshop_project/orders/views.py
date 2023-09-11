from django.shortcuts import render
from django.views import generic

from products.models import Product


class CartView(generic.ListView):
    template_name = "orders/cart.html"

    def get_queryset(self):
        return Product.objects.all()
