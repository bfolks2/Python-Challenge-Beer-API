# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 01:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mybeerapp', '0007_auto_20170912_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 14, 1, 58, 44, 64995, tzinfo=utc)),
        ),
    ]
