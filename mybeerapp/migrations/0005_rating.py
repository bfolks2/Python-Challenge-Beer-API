# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 01:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mybeerapp', '0004_auto_20170828_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aroma', models.PositiveIntegerField(choices=[(1, '1/5'), (2, '2/5'), (3, '3/5'), (4, '4/5'), (5, '5/5')])),
                ('appearance', models.PositiveIntegerField(choices=[(1, '1/5'), (2, '2/5'), (3, '3/5'), (4, '4/5'), (5, '5/5')])),
                ('taste', models.PositiveIntegerField(choices=[(1, '1/10'), (2, '2/10'), (3, '3/10'), (4, '4/10'), (5, '5/10'), (6, '6/10'), (7, '7/10'), (8, '8/10'), (9, '9/10'), (10, '10/10')])),
                ('palate', models.PositiveIntegerField(choices=[(1, '1/5'), (2, '2/5'), (3, '3/5'), (4, '4/5'), (5, '5/5')])),
                ('bottle_style', models.PositiveIntegerField(choices=[(1, '1/5'), (2, '2/5'), (3, '3/5'), (4, '4/5'), (5, '5/5')])),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='mybeerapp.Beer')),
            ],
        ),
    ]