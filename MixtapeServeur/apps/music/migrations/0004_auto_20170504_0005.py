# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_music_music_uri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='music_uri',
            field=models.CharField(default='NULL', max_length=400),
        ),
    ]
