# Generated by Django 5.0.6 on 2024-08-29 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0022_cuopon_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cuopon_code',
            new_name='coupon_code',
        ),
    ]
