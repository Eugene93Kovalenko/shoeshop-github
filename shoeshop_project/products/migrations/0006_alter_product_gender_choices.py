# Generated by Django 4.2.5 on 2023-09-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_gender_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender_choices',
            field=models.CharField(blank=True, choices=[('men', 'Men'), ('women', 'Women'), ('unisex', 'Unisex')], max_length=10),
        ),
    ]
