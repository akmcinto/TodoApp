# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 00:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_auto_20160126_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 26, 17, 23, 42, 694408), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 26, 17, 23, 42, 693908), verbose_name='date created'),
        ),
    ]