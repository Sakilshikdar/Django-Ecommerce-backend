# Generated by Django 5.0.1 on 2024-03-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amout',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
