# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20170109_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='history_img%Y-%m-%d'),
            preserve_default=False,
        ),
    ]
