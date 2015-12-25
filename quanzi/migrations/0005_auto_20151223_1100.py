# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanzi', '0004_auto_20151222_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
