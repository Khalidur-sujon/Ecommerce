# Generated by Django 4.2.1 on 2023-05-09 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_coupon'),
        ('carts', '0002_coupon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.coupon'),
        ),
    ]
