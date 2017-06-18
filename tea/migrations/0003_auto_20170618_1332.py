# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-18 18:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tea', '0002_teatype_steeping_time_minutes'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('user', 'tea')]),
        ),
    ]
