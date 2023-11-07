# Generated by Django 4.2.5 on 2023-10-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_alter_shippingaddress_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
                ('one_timer', models.BooleanField()),
            ],
        ),
    ]