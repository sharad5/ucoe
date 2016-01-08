# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0011_auto_20160108_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date_events',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
