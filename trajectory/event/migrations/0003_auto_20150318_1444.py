# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20150318_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='enddate',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='startdate',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
