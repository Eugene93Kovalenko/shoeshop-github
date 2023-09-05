from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):

    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']


# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     country = models.CharField(max_length=150, null=True)
#     city = models.CharField(max_length=150, null=True)
#     address = models.CharField(max_length=200, null=True)
#     zipcode = models.CharField(max_length=150, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = 'Адрес'
#         verbose_name_plural = 'Адреса'
#
#     def __str__(self) -> str:
#         return f"{self.zipcode}, {self.country}, {self.city}, {self.address}"
