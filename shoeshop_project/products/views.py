from django.shortcuts import render
from django.views import generic

from .models import *


class HomeView(generic.ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all()[:4]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShopView(generic.ListView):
    model = Product
    template_name = "products/shop.html"
    context_object_name = "products"
    paginate_by = 2

    def get_queryset(self):
        # if self.request.GET.get("ordering"):
        #     return Product.objects.filter(self.get_filters()).order_by(
        #         self.get_ordering()
        #     )
        # return Product.objects.filter(self.get_filters())
        return Product.objects.all()[:8]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
