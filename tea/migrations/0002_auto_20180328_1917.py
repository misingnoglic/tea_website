# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='description_directions',
            field=models.TextField(blank=True, null=True),
        ),
    ]