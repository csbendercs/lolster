# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 04:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optItem', '0002_summoner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='summoner',
            old_name='recentMatch',
            new_name='recentMatches',
        ),
    ]
