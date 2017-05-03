# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixtapeUser', '0003_auto_20170503_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mixtapeuser',
            old_name='fname',
            new_name='device',
        ),
        migrations.RenameField(
            model_name='mixtapeuser',
            old_name='lname',
            new_name='fb_id',
        ),
        migrations.AddField(
            model_name='mixtapeuser',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mixtapeuser',
            name='is_facebook_user',
            field=models.BooleanField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='mixtapeuser',
            name='profil_picture_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mixtapeuser',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
