# Generated by Django 5.1.1 on 2024-09-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_coupon_active_coupon_discount_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='certificate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='requisites',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]