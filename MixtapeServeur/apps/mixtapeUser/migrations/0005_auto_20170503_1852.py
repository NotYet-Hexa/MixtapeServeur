# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 18:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mixtapeUser', '0004_auto_20170503_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mixtapeuser',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='mixtapeuser',
            name='longitude',
        ),
    ]
