# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_auto_20160106_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]