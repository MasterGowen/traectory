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
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, default='None')),
                ('name', models.CharField(verbose_name='Название', max_length=1024, default='Ячейка')),
                ('events', models.ManyToManyField(to='event.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, default='None')),
                ('name', models.CharField(verbose_name='Название', max_length=1024, null=True, blank=True)),
                ('comment', models.TextField(verbose_name='Описание', max_length=4096, null=True, blank=True)),
                ('payd', models.BooleanField(verbose_name='Платно', default=False)),
                ('cells', models.ManyToManyField(to='trajectory.Cell')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trajectory',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, default='None')),
                ('comment', models.CharField(max_length=2048, null=True, blank=True)),
                ('user_id', models.CharField(max_length=32, default='None')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
