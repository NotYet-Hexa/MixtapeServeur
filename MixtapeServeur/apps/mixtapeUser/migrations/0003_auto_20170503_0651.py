# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixtapeUser', '0002_auto_20170423_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mixtapeuser',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mixtapeuser',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
