# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanzi', '0006_auto_20151223_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Praise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('praised', models.ForeignKey(related_name='to', to='quanzi.Share')),
                ('praiser', models.ForeignKey(related_name='from+', to='quanzi.User')),
            ],
        ),
    ]
