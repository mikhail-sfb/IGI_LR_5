# Generated by Django 5.0.5 on 2024-05-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_remove_coupon_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='discount_amount',
            field=models.IntegerField(default=0),
        ),
    ]