# Generated by Django 5.0.5 on 2024-05-22 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_contact_employer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='active',
        ),
    ]
