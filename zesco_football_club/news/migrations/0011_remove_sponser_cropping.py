# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 09:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20170103_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponser',
            name='cropping',
        ),
    ]