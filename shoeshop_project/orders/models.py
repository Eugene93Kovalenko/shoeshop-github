from django.db import models
from django_countries.fields import CountryField

from config import settings
from products.models import *


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} pcs | {self.product_variation.product.name} | {self.product_variation.size} size |" \
               f" {self.user}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def get_total_product_price(self):
        if self.product_variation.product.discount_price:
            return self.quantity * self.product_variation.product.discount_price
        return self.quantity * self.product_variation.product.price

    def get_remove_from_cart_url(self):
        return reverse("orders:remove-from-cart", kwargs={"slug": self.product_variation.product.slug})


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    delivery_price = models.DecimalField(default=50, max_digits=7, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)

    # payment = models.ForeignKey(
    #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    # coupon = models.ForeignKey(
    #     'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    # being_delivered = models.BooleanField(default=False)
    # received = models.BooleanField(default=False)
    # refund_requested = models.BooleanField(default=False)
    # refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} | Ordered: {self.ordered}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    # def get_total(self):
    #     total = 0
    #     for order_item in self.items.all():
    #         total += order_item.get_final_price()
    #     if self.coupon:
    #         total -= self.coupon.amount
    #     return total


class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = CountryField(multiple=False)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.user} | {self.city} | {self.address}'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return self.user
