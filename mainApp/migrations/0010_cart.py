# Generated by Django 3.1.7 on 2021-03-26 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_auto_20210325_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
            ],
        ),
    ]
