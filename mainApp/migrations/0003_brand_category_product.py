# Generated by Django 3.1.7 on 2021-03-24 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20210323_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('color', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('color1', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('color2', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('color3', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('color4', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('color5', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('size1', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('size2', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('size3', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('size4', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('size5', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('img4', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('img5', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
    ]
