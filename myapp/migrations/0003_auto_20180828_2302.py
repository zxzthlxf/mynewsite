# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Meduim'), ('L', 'Large')], max_length=1),
        ),
    ]
