# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traectory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traectory',
            name='id',
            field=models.CharField(default='6f1bdce3e3a9914506ede261db9d4da7', primary_key=True, serialize=False, max_length=32),
            preserve_default=True,
        ),
    ]
