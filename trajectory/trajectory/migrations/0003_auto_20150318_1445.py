# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trajectory', '0002_auto_20150318_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell',
            name='step',
            field=models.IntegerField(blank=True, null=True, max_length=8),
            preserve_default=True,
        ),
    ]
