# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20161105_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatcher', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='crisis',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='crisis',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dispatch',
            name='crisis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Crisis'),
        ),
    ]
