from django.db import models

from config import settings
from products.models import Product


# class OrderItem(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     # order = models.ForeignKey('Order', )
#     ordered = models.BooleanField(default=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.quantity} of {self.product.name}"
#
#     def get_total_item_price(self):
#         return self.quantity * self.product.price
#
#     def get_total_discount_item_price(self):
#
#         return self.quantity * self.product.discount_price
#
#     def get_final_price(self):
#         if self.product.discount_price:
#             return self.get_total_discount_item_price()
#         return self.get_total_item_price()
#
#
# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     ref_code = models.CharField(max_length=20, blank=True, null=True)
#     items = models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#     shipping_address = models.ForeignKey(
#         'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
#     billing_address = models.ForeignKey(
#         'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
#     payment = models.ForeignKey(
#         'Payment', on_delete=models.SET_NULL, blank=True, null=True)
#     # coupon = models.ForeignKey(
#     #     'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
#     being_delivered = models.BooleanField(default=False)
#     received = models.BooleanField(default=False)
#     refund_requested = models.BooleanField(default=False)
#     refund_granted = models.BooleanField(default=False)
#
#     '''
#     1. Item added to cart
#     2. Adding a billing address
#     (Failed checkout)
#     3. Payment
#     (Preprocessing, processing, packaging etc.)
#     4. Being delivered
#     5. Received
#     6. Refunds
#     '''
#
#     def __str__(self):
#         return self.user.username
#
#     def get_total(self):
#         total = 0
#         for order_item in self.items.all():
#             total += order_item.get_final_price()
#         if self.coupon:
#             total -= self.coupon.amount
#         return total
