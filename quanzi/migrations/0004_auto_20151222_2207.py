# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanzi', '0003_auto_20151221_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='news',
            name='padate',
        ),
        migrations.RemoveField(
            model_name='news',
            name='praise_count',
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='news',
            name='number',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='hobby',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
