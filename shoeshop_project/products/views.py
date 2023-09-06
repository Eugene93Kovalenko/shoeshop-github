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
        context['brands_list'] = [product.brand for product in Product.objects.all()]
        context['categories_list'] = [product.category for product in Product.objects.all()]
        context['stiles_list'] = [product.style for product in Product.objects.all()]
        context['materials_list'] = [product.get_material_display for product in Product.objects.all()]
        context['colors_list'] = [product.get_color_display for product in Product.objects.all()]
        context['sizes_list'] = [product.size for product in SizeVariation.objects.distinct('size')]
        print(context['sizes_list'])
        return context
