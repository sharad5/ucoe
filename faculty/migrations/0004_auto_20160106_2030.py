# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_auto_20160106_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]