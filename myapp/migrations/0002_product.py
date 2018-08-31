# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('size', models.CharField(choices=[('S', 'Smaill'), ('M', 'Meduim'), ('L', 'Large')], max_length=1)),
            ],
        ),
    ]
