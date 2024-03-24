# Generated by Django 5.0.1 on 2024-03-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_vendor_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publish_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]