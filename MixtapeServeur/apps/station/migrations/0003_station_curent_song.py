# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0002_auto_20170503_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='curent_song',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]
