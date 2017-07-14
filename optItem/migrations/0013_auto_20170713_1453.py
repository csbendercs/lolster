# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-14 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optItem', '0012_match_gameversion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='champ10ItemList',
            field=models.ManyToManyField(related_name='champ10ItemList', to='optItem.Item'),
        ),
        migrations.AlterField(
            model_name='match',
            name='champ1ItemList',
            field=models.ManyToManyField(related_name='champ1ItemList', to='optItem.Item'),
        ),
        migrations.AlterField(
            model_name='match',
            name='champ2ItemList',
            field=models.ManyToManyField(related_name='champ2ItemList', to='optItem.Item'),
        ),
        migrations.AlterField(
            model_name='match',
            name='champ3ItemList',
            field=models.ManyToManyField(related_name='champ3ItemList', to='optItem.Item'),
        ),
        migrations.AlterField(
            model_name='match',
            name='champ4ItemList',
            field=models.ManyToManyField(related_name='champ4ItemList', to='optItem.Item'),
        ),
        migrations.AlterField(
            model_name='match',
            name='champ5ItemList',
            field=models.ManyToManyField(related_name='champ5ItemList', to='optItem.Item'),
        ),
        migrations.AlterField(
            model_name='match',
            name='champ6ItemList',
            field=models.ManyToManyField(related_name='champ6ItemList', to='optItem.Item'),
        ),
        migrations.AlterField(
            model_name='match',
            name='champ7ItemList',
            field=models.ManyToManyField(related_name='champ7ItemList', to='optItem.Item'),
        ),
        migrations.AlterField(
            model_name='match',
            name='champ8ItemList',
            field=models.ManyToManyField(related_name='champ8ItemList', to='optItem.Item'),
        ),
        migrations.AlterField(
            model_name='match',
            name='champ9ItemList',
            field=models.ManyToManyField(related_name='champ9ItemList', to='optItem.Item'),
        ),
    ]