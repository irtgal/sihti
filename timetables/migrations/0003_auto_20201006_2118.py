# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-10-06 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0002_day_finnished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='finnished',
            field=models.CharField(blank=True, choices=[('y', 'yes'), ('m', 'maybe'), ('n', 'no')], max_length=1, null='True'),
        ),
    ]
