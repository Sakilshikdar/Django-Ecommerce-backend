# Generated by Django 5.0.1 on 2024-03-23 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_product_publish_status_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
