# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybeerapp', '0002_auto_20170828_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glass',
            options={'verbose_name_plural': 'glasses'},
        ),
        migrations.RemoveField(
            model_name='glass',
            name='beer',
        ),
        migrations.AddField(
            model_name='glass',
            name='beer',
            field=models.ManyToManyField(to='mybeerapp.Beer'),
        ),
    ]