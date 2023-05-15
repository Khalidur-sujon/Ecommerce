# Generated by Django 4.2.1 on 2023-05-09 08:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('uid', models.CharField(default=uuid.uuid4, editable=False, max_length=200, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coupon_code', models.CharField(max_length=20)),
                ('is_expired', models.BooleanField(default=False)),
                ('discount_amount', models.IntegerField(default=False)),
                ('minimum_amount', models.IntegerField(default=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
