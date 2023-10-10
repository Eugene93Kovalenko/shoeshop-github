from decimal import Decimal

import stripe
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from accounts.models import CustomUser
from orders.cart import Cart
from orders.forms import CheckoutForm
from orders.models import *


class CartView(generic.ListView):
    template_name = "orders/cart.html"
    context_object_name = 'cart_items'

    def get_queryset(self):
        # cart = Cart(self.request)
        # print(cart)
        # print(list(Cart(self.request)))
        return Cart(self.request)


@require_POST
def add_to_cart(request, slug):
    cart = Cart(request)
    if request.POST.get('quantity') == '0' or not request.POST.get('product-size'):
        messages.warning(request, "Вы должны выбрать размер и количество товара")
        return redirect(request.META.get('HTTP_REFERER'))
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product-size')
    product_variation = get_object_or_404(ProductVariation, product__slug=slug, size__name=size)
    # product_variation = ProductVariation.objects.filter(product__slug=slug, size__name=size)
    if product_variation.quantity < quantity:
        messages.warning(request, "На складе нет этого товара в таком количестве")
        return redirect(request.META.get('HTTP_REFERER'))
    cart.add(product_variation=product_variation, quantity=quantity, user=request.user.username)
    return redirect("products:home")


def remove_from_cart(request, slug):
    cart = Cart(request)
    if request.method == 'POST':
        size = request.POST.get('size')
        product_variation = get_object_or_404(ProductVariation, product__slug=slug, size__name=size)
        cart.delete(product_variation=product_variation)
        return redirect("orders:cart")


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
    # def get_form_kwargs(self):
    #     kwargs = super(CheckoutView, self).get_form_kwargs()
    #     kwargs["user_id"] = self.request.user.id
    #     return kwargs
    #
    # def get_context_data(self, **kwargs):
    #     context = super(CheckoutView, self).get_context_data(**kwargs)
    #     context["order"] = get_or_set_order_session(self.request)
    #     return context


class PaymentView(generic.TemplateView):
    template_name = "orders/payment.html"


class OrderCompleteView(generic.TemplateView):
    template_name = "orders/order-complete.html"


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateStripeCheckoutSessionView(generic.View):
    def post(self, request):
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=self.get_line_items_list(),
            mode='payment',
            metadata=self.get_metadata(),
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
            customer_email=self.get_user_email()
        )
        return redirect(checkout_session.url)

    def get_metadata(self):
        cart = Cart(self.request)
        metadata = {}
        for item in cart:
            metadata[item['product_variation'].id] = item['quantity']
        return metadata

    def get_line_items_list(self):
        cart = Cart(self.request)
        line_items_list = []
        for item in cart:
            line_items_list.append(
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(item['price']) * 100,
                        'product_data': {
                            'name': item['product_variation'].product.name
                        },
                    },
                    'quantity': item['quantity'],
                }
            )
        return line_items_list

    def get_user_email(self):
        if self.request.user.is_authenticated:
            return self.request.user.email


class SuccessView(generic.TemplateView):
    template_name = "orders/success.html"


class CancelView(generic.TemplateView):
    template_name = "orders/cancel.html"


@method_decorator(csrf_exempt, name="dispatch")
class StripeWebhookView(generic.View):
    """
    Stripe webhook view to handle checkout session completed event.
    """
    def post(self, request, format=None):
        payload = request.body
        endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
        sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
        event = None

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)

        if event["type"] == "checkout.session.completed":
            print("Payment successful")
            session = event["data"]["object"]
            customer_email = session["customer_details"]["email"]
            amount = session['amount_total']
            user = CustomUser.objects.get(email=customer_email)
            ordered_date = timezone.now()
            order = Order.objects.create(
                user=user, ordered_date=ordered_date, ordered=True)
            for key, value in session['metadata'].items():
                order_item = OrderItem.objects.create(user=user,
                                                      product_variation=ProductVariation.objects.get(id=key),
                                                      quantity=value,
                                                      ordered=True
                                                      )
                order.products.add(order_item)
            Payment.objects.create(
                stripe_charge_id=session['id'],
                user=user,
                order=order,
                amount=amount / 100,
            )
        return HttpResponse(status=200)
