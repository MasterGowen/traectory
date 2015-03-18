# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(serialize=False, max_length=32, default='None', primary_key=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=1024)),
                ('comment', models.TextField(null=True, max_length=4096, verbose_name='Описание', blank=True)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/%Y/%m', verbose_name='Image', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
