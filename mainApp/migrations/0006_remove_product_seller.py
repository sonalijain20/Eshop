# Generated by Django 3.1.7 on 2021-03-24 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
    ]