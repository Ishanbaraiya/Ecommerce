# Generated by Django 5.0.6 on 2024-08-31 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0024_billing_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing_detail',
            old_name='city',
            new_name='district',
        ),
    ]
