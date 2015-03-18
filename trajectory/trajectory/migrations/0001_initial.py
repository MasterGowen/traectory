# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.CharField(max_length=32, default='None', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024, default='Ячейка', verbose_name='Название')),
                ('events', models.ManyToManyField(to='event.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.CharField(max_length=32, default='None', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024, verbose_name='Название', null=True, blank=True)),
                ('comment', models.TextField(max_length=4096, verbose_name='Описание', null=True, blank=True)),
                ('payd', models.BooleanField(default=False, verbose_name='Платно')),
                ('cells', models.ManyToManyField(to='trajectory.Cell')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trajectory',
            fields=[
                ('id', models.CharField(max_length=32, default='None', primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=22048, null=True, blank=True)),
                ('user_id', models.CharField(max_length=32, default='None')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
