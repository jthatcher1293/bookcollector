# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-20 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviecollection', '0004_auto_20171019_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='disc_format',
            field=models.CharField(choices=[('blu_ray', 'Blu-Ray'), ('dvd', 'DVD'), ('mixed', 'Blu-Ray/DVD')], default='dvd', max_length=10),
        ),
    ]