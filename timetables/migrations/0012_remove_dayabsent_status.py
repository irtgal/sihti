# Generated by Django 3.1.2 on 2020-11-24 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0011_auto_20201123_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayabsent',
            name='status',
        ),
    ]
