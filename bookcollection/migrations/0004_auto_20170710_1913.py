# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-10 19:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0003_book_authors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
    ]
