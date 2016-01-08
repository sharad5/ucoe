# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0007_auto_20160107_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='event_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='gallery_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slide_image1',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slide_image2',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slide_image3',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]