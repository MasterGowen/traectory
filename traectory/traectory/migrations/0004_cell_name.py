# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traectory', '0003_auto_20150305_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='name',
            field=models.CharField(default='Ячейка', verbose_name='Название', max_length=1024),
            preserve_default=True,
        ),
    ]
