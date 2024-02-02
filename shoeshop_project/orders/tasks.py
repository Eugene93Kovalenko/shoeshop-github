from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_order_conformation_mail(user_name, user_email):
    body = f"""
        Hi {user_name}!\n\n
        Thank you for your purchase!\n\n
        
    """
    # TODO item, quantity, total price
    send_mail('ShoeShop purchase', body, None, [user_email], fail_silently=False)
