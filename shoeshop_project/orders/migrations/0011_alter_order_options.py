# Generated by Django 4.2.5 on 2023-09-18 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_remove_orderitem_delivery_price_order_delivery_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]