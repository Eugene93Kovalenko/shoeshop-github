from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views import generic

from orders.models import *
from products.models import Product


class CartView(generic.ListView):
    template_name = "orders/cart.html"
    context_object_name = 'cart_items'

    # def add_to_cart(self):
    #     OrderItem.objects.create(user=self.request.user, product_variation=)

    def get_queryset(self):
        print(self.request.GET.get('product-size'))
        print(self.request.GET.get('quantity'))
        return OrderItem.objects.filter()


def get_product_variation_size(request, slug):
    print('-------------')
    size = request.GET.get('product-size')
    return reverse("orders:add-to-cart", kwargs={"slug": slug, "size": size})


def add_to_cart(request, slug, size):    ######
    print('++++++++++++++++++')
    # size = request.GET.get('product-size')
    # print(size)
    product_variation = get_object_or_404(ProductVariation, product__slug=slug, size__name=size)    #######
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        product_variation=product_variation
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product_variation__product__slug=product_variation.product.slug).exists():
            order_item.quantity += 1
            order_item.save()
            # messages.info(request, "This item quantity was updated.")
            return redirect("orders:cart")
        else:
            order.products.add(order_item)
            # messages.info(request, "This item was added to your cart.")
            return redirect("orders:cart")
    else:
        order = Order.objects.create(
            user=request.user, ordered_date=timezone.now())
        order.products.add(order_item)
        # messages.info(request, "This item was added to your cart.")
        return redirect("orders:cart")
