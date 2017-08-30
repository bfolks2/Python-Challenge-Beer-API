# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mybeerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='beer',
            name='glass_type',
        ),
        migrations.AddField(
            model_name='glass',
            name='beer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glass', to='mybeerapp.Beer'),
        ),
    ]
