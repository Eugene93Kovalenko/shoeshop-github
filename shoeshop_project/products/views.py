from time import timezone

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from orders.models import OrderItem, Order
from .filters import ProductFilter
from .models import *


class HomeView(generic.ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all()[:16]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShopView(generic.ListView):
    model = Product
    template_name = "products/shop.html"
    context_object_name = "products"
    paginate_by = 2

    def get_filters(self):
        brand_q, color_q, material_q, size_q = Q(), Q(), Q(), Q()

        for brand in self.request.GET.getlist('brand'):
            if brand:
                brand_q |= Q(brand__name=brand)

        for material in self.request.GET.getlist('material'):
            if material:
                material_q |= Q(material__name=material)

        for color in self.request.GET.getlist('color'):
            if color:
                color_q |= Q(color__name=color)

        for size in self.request.GET.getlist('size'):
            if size:
                size_q |= Q(size=size)

        return brand_q & color_q & material_q & size_q

    def get_queryset(self):
        return Product.objects.filter(self.get_filters())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['brands_list'] = set([product.brand for product in Product.objects.all()])
        context['brands_list'] = Brand.objects.all()
        # context['sizes_list'] = [product.size for product in SizeVariation.objects.distinct('size')]
        context['sizes_list'] = Size.objects.all()
        # context['categories_list'] = [product.category for product in Product.objects.all()]
        context['categories_list'] = Category.objects.all()
        # context['colors_list'] = set([product.get_color_display for product in Product.objects.all()])
        context['colors_list'] = Color.objects.all()
        # context['materials_list'] = set([product.get_material_display for product in Product.objects.all()])
        context['materials_list'] = Material.objects.all()
        context['stiles_list'] = Style.objects.all()
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product-detail.html"
    context_object_name = "product"
    slug_url_kwarg = "product_slug"

    # def get_queryset(self):
    #     return ProductVariation.objects.filter(product__slug=self.kwargs["product_slug"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImage.objects.filter(product__slug=self.kwargs["product_slug"])
        context['sizes_per_product_list'] = [product.size for product in ProductVariation.objects.filter(
            product__slug=self.kwargs["product_slug"])]
        return context


class AboutView(generic.TemplateView):
    template_name = "products/about.html"


class ContactView(generic.TemplateView):
    template_name = "products/contact.html"
