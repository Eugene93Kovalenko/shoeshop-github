from django.contrib import admin

from orders.models import *

admin.site.register(OrderItem)
admin.site.register(Order)
