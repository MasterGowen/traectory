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
                ('id', models.CharField(serialize=False, default='None', max_length=32, primary_key=True)),
                ('name', models.CharField(verbose_name='Название', max_length=4096)),
                ('file', models.FileField(verbose_name='User file', upload_to='files/%Y/%m')),
                ('date', models.DateField(default=datetime.datetime(2015, 3, 18, 18, 24, 59, 83442), auto_now_add=True)),
                ('user', models.ForeignKey(to='user.User', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
