# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20161123_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='favori',
            name='comment',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
    ]
