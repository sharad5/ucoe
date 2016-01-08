# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 19:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_post_highlight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_highlight',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='author_highlights',
            field=models.CharField(default=datetime.datetime(2016, 1, 6, 19, 54, 50, 361557, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='author_notice',
            field=models.CharField(default=datetime.datetime(2016, 1, 6, 19, 55, 4, 216512, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='created_date_highlights',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='created_date_notice',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='text_highlights',
            field=models.TextField(default=datetime.datetime(2016, 1, 6, 19, 55, 8, 90837, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='text_notice',
            field=models.TextField(default=datetime.datetime(2016, 1, 6, 19, 55, 13, 20676, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_highlights',
            field=models.CharField(default=datetime.datetime(2016, 1, 6, 19, 55, 16, 762343, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_notice',
            field=models.CharField(default=datetime.datetime(2016, 1, 6, 19, 55, 19, 778296, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Post_Highlight',
        ),
    ]