# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20160105_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about', models.TextField()),
                ('dept_history', models.TextField()),
                ('infra', models.TextField()),
                ('labs', models.TextField()),
                ('hostel', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='About_home',
        ),
        migrations.DeleteModel(
            name='Dept_history',
        ),
        migrations.DeleteModel(
            name='Hostel',
        ),
        migrations.DeleteModel(
            name='Infrastructure',
        ),
        migrations.DeleteModel(
            name='Labs',
        ),
    ]
