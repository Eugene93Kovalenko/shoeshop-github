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
        print(self.request.GET.get('color'))
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImage.objects.filter(product__slug=self.kwargs["product_slug"])
        context['sizes_per_product_list'] = [product.size for product in ProductVariation.objects.distinct('size')]
        context['product_variation'] = ProductVariation.objects.filter(product__slug=self.kwargs["product_slug"])[0]
        # context['s'] = self.request.session.get('cart')
        # print(context['s'])
        # print(context['product_variation'])
        return context


class AboutView(generic.TemplateView):
    template_name = "products/about.html"


class ContactView(generic.TemplateView):
    template_name = "products/contact.html"


# @login_required
def add_to_cart(request, s, size):
    print('---------------')
    product_variation = get_object_or_404(ProductVariation, product__slug=s, size__name=size)
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        product_variation=product_variation,
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product_variation.slug).exists():
            order_item.quantity += 1
            order_item.save()
            # messages.info(request, "This item quantity was updated.")
            return redirect("orders:cart")
        else:
            order.products.add(order_item)
            # messages.info(request, "This item was added to your cart.")
            return redirect("orders:cart")
    else:
        # ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=timezone.now())
        order.products.add(order_item)
        # messages.info(request, "This item was added to your cart.")
        return redirect("orders:cart")




