# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170420_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messcut',
            name='days',
            field=models.IntegerField(),
        ),
    ]