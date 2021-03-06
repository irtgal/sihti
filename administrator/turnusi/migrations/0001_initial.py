# Generated by Django 3.1.2 on 2020-12-10 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timetables', '0013_auto_20201205_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('group', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='timetables.group')),
            ],
            options={
                'verbose_name_plural': 'Turnuses',
            },
        ),
        migrations.CreateModel(
            name='TurnusShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, choices=[('Mon', 'Pon'), ('Tue', 'Tor'), ('Wed', 'Sre'), ('Thu', 'Čet'), ('Fri', 'Pet'), ('Sat', 'Sob'), ('Sun', 'Ned')], max_length=3, null=True)),
                ('start', models.TimeField(blank=True, null=True)),
                ('end', models.TimeField(blank=True, null=True)),
                ('shift_class', models.CharField(blank=True, choices=[('y', 'yes'), ('m', 'maybe'), ('n', 'no')], max_length=1, null=True)),
                ('employee', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('turnus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='turnusi.turnus')),
            ],
        ),
    ]
