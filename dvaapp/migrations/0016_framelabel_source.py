# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0015_auto_20170222_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='framelabel',
            name='source',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]