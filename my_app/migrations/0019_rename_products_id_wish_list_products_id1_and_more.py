# Generated by Django 5.0.6 on 2024-08-24 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0018_wish_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish_list',
            old_name='products_id',
            new_name='products_id1',
        ),
        migrations.RenameField(
            model_name='wish_list',
            old_name='user_id',
            new_name='user_id1',
        ),
    ]
