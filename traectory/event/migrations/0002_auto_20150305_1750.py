# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='comment',
            field=models.TextField(max_length=4096, verbose_name='Описание'),
            preserve_default=True,
        ),
    ]
