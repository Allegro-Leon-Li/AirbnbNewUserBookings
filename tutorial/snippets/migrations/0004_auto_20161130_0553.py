# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20161129_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='location',
            field=models.CharField(blank=True, choices=[('US', 'US'), ('DE', 'Germany'), ('AU', 'Australia'), ('CA', 'Canada'), ('FR', 'France'), ('GB', 'Britain'), ('ES', 'Spain'), ('PT', 'Portugal'), ('NL', 'Netherlands'), ('OT', 'Others')], default='us', max_length=100),
        ),
    ]