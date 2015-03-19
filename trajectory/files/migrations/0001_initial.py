# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.CharField(primary_key=True, default='None', max_length=32, serialize=False)),
                ('name', models.CharField(max_length=4096, verbose_name='Название')),
                ('file', models.FileField(upload_to='files/%Y/%m', verbose_name='User file')),
                ('date', models.DateField(default=datetime.datetime(2015, 3, 19, 14, 2, 17, 220172), auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, to='user.User', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
