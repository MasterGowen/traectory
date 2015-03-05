# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('i', models.CharField(max_length=1024)),
                ('f', models.CharField(max_length=1024)),
                ('o', models.CharField(max_length=1024)),
                ('city', models.CharField(max_length=1024)),
                ('email', models.EmailField(max_length=1024)),
                ('tel', models.CharField(max_length=1024)),
                ('status', models.CharField(choices=[('online', 'Заочно'), ('offline', 'Очно')], max_length=7, default='offline')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
