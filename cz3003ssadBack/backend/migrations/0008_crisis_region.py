# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20161106_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='crisis',
            name='region',
            field=models.CharField(default='Central', max_length=10),
            preserve_default=False,
        ),
    ]