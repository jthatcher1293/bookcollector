# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-18 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('series_number', models.IntegerField(blank=True, null=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecollection.Genre')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecollection.Series'),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together=set([('title', 'year')]),
        ),
    ]
