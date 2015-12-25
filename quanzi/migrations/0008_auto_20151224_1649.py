# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanzi', '0007_praise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commend',
            name='Commender',
            field=models.ForeignKey(related_name='commender', to='quanzi.User'),
        ),
    ]
