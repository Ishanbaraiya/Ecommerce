# Generated by Django 5.0.6 on 2024-09-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0026_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
