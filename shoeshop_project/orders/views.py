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


class RemoveFromCartView(generic.View):
    @staticmethod
    def get(request, *args, **kwargs):
        size = request.GET.get('size')
        product_variation = get_object_or_404(ProductVariation, product__slug=kwargs['slug'], size__name=size)
        order_item = get_object_or_404(OrderItem, product_variation=product_variation,
                                       user=request.user,
                                       ordered=False)
        order_item.delete()
        return redirect("orders:cart")


class CheckoutView(generic.FormView):
    template_name = "orders/checkout.html"
    form_class = CheckoutForm
    # success_url = reverse("orders:order-complete", kwargs={})

    def get_success_url(self) -> str:
        return reverse("orders:payment")

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


class OrderCompleteView(generic.TemplateView):
    template_name = "orders/order-complete.html"



