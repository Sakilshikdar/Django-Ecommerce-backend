# Generated by Django 5.0.1 on 2024-02-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_product_demo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phome',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.PositiveBigIntegerField(null=True, unique=True),
        ),
    ]
