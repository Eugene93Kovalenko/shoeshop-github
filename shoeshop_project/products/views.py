from django.db.models import Q
from django.shortcuts import render
from django.views import generic

from .filters import ProductFilter
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

    def get_filters(self):
        brand_q, color_q, material_q = Q(), Q(), Q()

        for brand in self.request.GET.getlist('brand'):
            if brand:
                brand_q |= Q(brand__name=brand)

        for material in self.request.GET.getlist('material'):
            if material:
                material_q |= Q(material=material)

        for color in self.request.GET.getlist('color'):
            if color:
                color_q |= Q(color=color)

        return brand_q & color_q & material_q

    def get_queryset(self):
        return Product.objects.filter(self.get_filters())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands_list'] = [product.brand for product in Product.objects.all()]
        context['categories_list'] = [product.category for product in Product.objects.all()]
        context['stiles_list'] = [product.style for product in Product.objects.all()]
        context['materials_list'] = [product.get_material_display for product in Product.objects.all()]
        context['colors_list'] = [product.get_color_display for product in Product.objects.all()]
        print(context['colors_list'])
        context['sizes_list'] = [product.size for product in SizeVariation.objects.distinct('size')]
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product-detail.html"
    context_object_name = "product"
    slug_url_kwarg = "product_slug"

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs["product_slug"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImage.objects.filter(product__slug=self.kwargs["product_slug"])
        # context["product_images"] = ProductImage.objects.filter(product__slug='women_boots')

        return context
