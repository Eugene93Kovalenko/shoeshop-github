# Generated by Django 4.2.5 on 2023-10-21 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_alter_review_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='rate',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='content',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='author',
            new_name='user',
        ),
    ]
