# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 03:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_sponser'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponser',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 1, 3, 3, 30, 24, 24553, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
