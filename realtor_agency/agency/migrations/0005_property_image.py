# Generated by Django 5.0.5 on 2024-05-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_alter_buyer_phone_number_alter_employee_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, upload_to='property_images/'),
        ),
    ]