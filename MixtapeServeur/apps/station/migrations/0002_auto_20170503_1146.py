# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='mac_address',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
    ]
