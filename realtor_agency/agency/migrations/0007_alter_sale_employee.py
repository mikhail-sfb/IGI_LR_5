# Generated by Django 5.0.5 on 2024-05-20 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0006_alter_sale_buyer_delete_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='agency.employer'),
        ),
    ]
