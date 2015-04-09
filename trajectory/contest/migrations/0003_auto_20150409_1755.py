# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_auto_20150409_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestitem',
            name='route',
            field=models.CharField(max_length=2, verbose_name='Направление', choices=[('01', 'Лучший электронный курс'), ('02', 'Лучшее ввизуальное оформление курса'), ('03', 'Лучшая инновация в контроле знаний')]),
            preserve_default=True,
        ),
    ]
