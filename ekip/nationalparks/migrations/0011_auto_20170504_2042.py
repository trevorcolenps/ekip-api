# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-04 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalparks', '0010_auto_20150902_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='federalsite',
            name='slug',
            field=models.SlugField(max_length=128, null=True, unique=True),
        ),
    ]
