# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-10-06 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0003_auto_20201006_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='finnished',
            field=models.CharField(blank=True, choices=[('y', 'yes'), ('m', 'maybe'), ('n', 'no')], max_length=1, null='True'),
        ),
    ]
