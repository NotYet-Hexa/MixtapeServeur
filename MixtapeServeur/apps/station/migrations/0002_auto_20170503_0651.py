# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='station',
            name='longitude',
            field=models.FloatField(),
        ),
    ]