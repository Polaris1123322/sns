# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanzi', '0005_auto_20151223_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fansnum',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='user',
            name='friendsnum',
            field=models.IntegerField(default=b'0'),
        ),
    ]
