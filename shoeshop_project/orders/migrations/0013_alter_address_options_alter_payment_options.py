# Generated by Django 4.2.5 on 2023-09-18 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_order_options_alter_orderitem_options_payment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Оплата', 'verbose_name_plural': 'Оплаты'},
        ),
    ]