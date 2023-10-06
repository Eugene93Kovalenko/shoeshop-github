from decimal import Decimal

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import generic
from django.views.decorators.http import require_POST

from orders.cart import Cart
from orders.forms import CheckoutForm
from orders.models import *


class CartView(generic.ListView):
    template_name = "orders/cart.html"
    context_object_name = 'cart_items'

    def get_queryset(self):
        cart = Cart(self.request)
        return cart


@require_POST
def add_to_cart(request, slug):
    cart = Cart(request)
    if request.POST.get('quantity') == '0' or not request.POST.get('product-size'):
        messages.warning(request, "Вы должны выбрать размер и количество товара")
        return redirect(request.META.get('HTTP_REFERER'))
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product-size')
    product_variation = get_object_or_404(ProductVariation, product__slug=slug, size__name=size)
    if product_variation.quantity < quantity:
        messages.warning(request, "На складе нет этого товара в таком количестве")
        return redirect(request.META.get('HTTP_REFERER'))
    cart.add(product_variation=product_variation, quantity=quantity, user=request.user.username)
    return redirect("orders:cart")


def remove_from_cart(request, slug):
    cart = Cart(request)
    if request.method == 'POST':
        size = request.POST.get('size')
        product_variation = get_object_or_404(ProductVariation, product__slug=slug, size__name=size)
        cart.delete(product_variation=product_variation)
        return redirect("orders:cart")


# def add_to_cart(request, slug):
#     if request.GET.get('quantity') == '0':
#         return redirect(request.META.get('HTTP_REFERER'))
#     quantity = int(request.GET.get('quantity'))
#     size = request.GET.get('product-size')
#     product_variation = get_object_or_404(ProductVariation, product__slug=slug, size__name=size)
#     if product_variation.quantity < quantity:
#         raise ValueError('На складе нет этого товара в таком количестве')
#     order_item, created = OrderItem.objects.get_or_create(
#         user=request.user,
#         product_variation=product_variation
#     )
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.products.filter(product_variation__product__slug=slug,
#                                  product_variation__size__name=size).exists():
#             order_item.quantity += quantity
#             order_item.save()
#             return redirect("orders:cart")
#         else:
#             order.products.add(order_item)
#             return redirect("orders:cart")
#     else:
#         order = Order.objects.create(
#             user=request.user, ordered_date=timezone.now())
#         order.products.add(order_item)
#         return redirect("orders:cart")


# class RemoveFromCartView(generic.View):
#     @staticmethod
#     def get(request, *args, **kwargs):
#         size = request.GET.get('size')
#         product_variation = get_object_or_404(ProductVariation, product__slug=kwargs['slug'], size__name=size)
#         order_item = get_object_or_404(OrderItem, product_variation=product_variation,
#                                        user=request.user,
#                                        ordered=False)
#         order_item.delete()
#         return redirect("orders:cart")


class CheckoutView(CartView, generic.FormView):
    template_name = "orders/checkout.html"
    form_class = CheckoutForm
    # success_url = reverse("orders:order-complete", kwargs={})

    def get_success_url(self):
        return reverse("orders:payment")

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


    # def form_valid(self, form):
    #     order = get_or_set_order_session(self.request)
    #     selected_shipping_address = form.cleaned_data.get(
    #         'selected_shipping_address'
    #     )
    #     selected_billing_address = form.cleaned_data.get(
    #         'selected_billing_address'
    #     )
    #     if selected_shipping_address:
    #         order.shipping_address = selected_shipping_address
    #     else:
    #         address = Address.objects.create(
    #             address_type=Address.SHIPPING_ADDRESS_TYPE,
    #             user=self.request.user,
    #             address_line_1=form.cleaned_data['shipping_address_line_1'],
    #             address_line_2=form.cleaned_data['shipping_address_line_2'],
    #             zip_code=form.cleaned_data['shipping_zip_code'],
    #             city=form.cleaned_data['shipping_city'],
    #         )
    #         order.shipping_address = address
    #
    #     if selected_billing_address:
    #         order.billing_address = selected_billing_address
    #     else:
    #         address = Address.objects.create(
    #             address_type=Address.BILLING_ADDRESS_TYPE,
    #             user=self.request.user,
    #             address_line_1=form.cleaned_data['billing_address_line_1'],
    #             address_line_2=form.cleaned_data['billing_address_line_2'],
    #             zip_code=form.cleaned_data['billing_zip_code'],
    #             city=form.cleaned_data['billing_city'],
    #         )
    #         order.billing_address = address
    #
    #     order.save()
    #     messages.info(self.request, "You have successfully added your addresses")
    #     return super(CheckoutView, self).form_valid(form)
    #
    # def get_form_kwargs(self) -> Dict[str, Any]:
    #     kwargs = super(CheckoutView, self).get_form_kwargs()
    #     kwargs["user_id"] = self.request.user.id
    #     return kwargs
    #
    # def get_context_data(self, **kwargs) -> Dict[str, Any]:
    #     context = super(CheckoutView, self).get_context_data(**kwargs)
    #     context["order"] = get_or_set_order_session(self.request)
    #     return context

class PaymentView(generic.TemplateView):
    template_name = "orders/payment.html"


class OrderCompleteView(generic.TemplateView):
    template_name = "orders/order-complete.html"






