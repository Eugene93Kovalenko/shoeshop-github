from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views import generic

from orders.forms import CheckoutForm
from orders.models import *
from products.models import Product


class CartView(generic.ListView):
    template_name = "orders/cart.html"
    context_object_name = 'cart_items'

    def get_queryset(self):
        return OrderItem.objects.filter(user=self.request.user).order_by('-created_at')

    def get_total_discount(self):
        total_discount = 0
        for item in self.get_queryset():
            if item.product_variation.product.discount_price:
                total_discount += item.product_variation.product.price * item.quantity - item.product_variation.product.discount_price * item.quantity
        return total_discount

    def get_total_all_products_price(self):
        total_products_price = 0
        for item in self.get_queryset():
            total_products_price += item.get_total_product_price()
        return total_products_price

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["get_total_discount"] = self.get_total_discount()
        context["get_total_all_products_price"] = self.get_total_all_products_price()
        context["count_cart_items"] = OrderItem.objects.filter(user=self.request.user).count()
        print(context["count_cart_items"])
        if OrderItem.objects.filter(user=self.request.user, ordered=False):
            context["delivery_price"] = Order.objects.filter(user=self.request.user, ordered=False)[0].delivery_price
        else:
            context["delivery_price"] = 0.00
        context["get_final_order_products_price"] = context["get_total_all_products_price"] + context["delivery_price"]
        return context


def add_to_cart(request, slug):
    if request.GET.get('quantity') == '0':
        return redirect(request.META.get('HTTP_REFERER'))
    quantity = int(request.GET.get('quantity'))
    size = request.GET.get('product-size')
    product_variation = get_object_or_404(ProductVariation, product__slug=slug, size__name=size)
    if product_variation.quantity < quantity:
        raise ValueError('На складе нет этого товара в таком количестве')
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        product_variation=product_variation
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product_variation__product__slug=slug,
                                 product_variation__size__name=size).exists():
            order_item.quantity += quantity
            order_item.save()
            return redirect("orders:cart")
        else:
            order.products.add(order_item)
            return redirect("orders:cart")
    else:
        order = Order.objects.create(
            user=request.user, ordered_date=timezone.now())
        order.products.add(order_item)
        return redirect("orders:cart")


def remove_from_cart(request, slug):
    print('++++++')
    # size = request.GET.get('size')
    # product_variation = get_object_or_404(ProductVariation, product__slug=slug, size__name=size)
    # order_qs = Order.objects.filter(user=request.user, ordered=False)

    # if order_qs.exists():
    #     order = order_qs[0]
    #     if order.products.filter(product_variation__product__slug=slug,
    #                              product_variation__size__name=size).exists():
    #         order_item = OrderItem.objects.filter(
    #             product_variation=product_variation,
    #             user=request.user,
    #             ordered=False
    #         )[0]
    #         order.products.remove(order_item)
    #         order_item.delete()
    #         return redirect("orders:cart")
    #     else:
    #         return redirect("orders:cart")
    # else:
    #     return redirect("orders:cart")
    size = request.GET.get('size')
    product_variation = get_object_or_404(ProductVariation, product__slug=slug, size__name=size)
    order = Order.objects.get(user=request.user, ordered=False)
    order_item = OrderItem.objects.get(
        product_variation=product_variation,
        user=request.user,
        ordered=False
    )
    order.products.remove(order_item)
    order_item.delete()
    return redirect("orders:cart")


class CheckoutView(generic.FormView):
    template_name = "orders/checkout.html"
    form_class = CheckoutForm


class OrderCompleteView(generic.TemplateView):
    template_name = "orders/order-complete.html"



