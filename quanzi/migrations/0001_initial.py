# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=200)),
                ('Commender', models.ForeignKey(related_name='commender', to='quanzi.Commend')),
            ],
        ),
        migrations.CreateModel(
            name='Followship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=140)),
                ('datetime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('praise_count', models.IntegerField(default=b'0')),
                ('number', models.IntegerField()),
                ('content', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField()),
                ('padate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('praise_count', models.IntegerField(default=b'0')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=140)),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=20)),
                ('pw', models.CharField(max_length=30)),
                ('birthday', models.DateField(blank=True)),
                ('school', models.CharField(max_length=20)),
                ('is_boy', models.BooleanField()),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('hobby', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='talk',
            name='auth',
            field=models.ForeignKey(related_name='author', to='quanzi.User'),
        ),
        migrations.AddField(
            model_name='talk',
            name='news_id',
            field=models.ForeignKey(related_name='news', to='quanzi.News'),
        ),
        migrations.AddField(
            model_name='share',
            name='host',
            field=models.ForeignKey(related_name='host', to='quanzi.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='fromer',
            field=models.ForeignKey(related_name='fromer', to='quanzi.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='toer',
            field=models.ForeignKey(related_name='toer', to='quanzi.User'),
        ),
        migrations.AddField(
            model_name='followship',
            name='fans',
            field=models.ForeignKey(related_name='fans', blank=True, to='quanzi.User', null=True),
        ),
        migrations.AddField(
            model_name='followship',
            name='followed',
            field=models.ForeignKey(related_name='followed', to='quanzi.User'),
        ),
        migrations.AddField(
            model_name='commend',
            name='share_id',
            field=models.ForeignKey(related_name='share', to='quanzi.Share'),
        ),
    ]
