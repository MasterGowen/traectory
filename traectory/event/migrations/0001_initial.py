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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Имя')),
                ('comment', models.TextField(max_length=4096, verbose_name='Имя')),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
