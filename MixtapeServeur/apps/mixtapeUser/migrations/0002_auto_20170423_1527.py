# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 15:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mixtapeUser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mixtapeuser',
            old_name='nom',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='mixtapeuser',
            old_name='prenom',
            new_name='lname',
        ),
    ]
