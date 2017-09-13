# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mybeerapp', '0006_auto_20170912_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer',
            name='glass',
        ),
        migrations.AddField(
            model_name='beer',
            name='glass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='beers', to='mybeerapp.Glass'),
        ),
    ]
