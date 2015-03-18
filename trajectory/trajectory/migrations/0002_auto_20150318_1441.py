# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20150318_1441'),
        ('trajectory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='step',
            field=models.IntegerField(max_length=8, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trajectory',
            name='events',
            field=models.ManyToManyField(to='event.Event'),
            preserve_default=True,
        ),
    ]
