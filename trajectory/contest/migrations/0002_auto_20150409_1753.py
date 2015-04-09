# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestitem',
            name='route',
            field=models.CharField(verbose_name='Направление', max_length=2, choices=[('Лучший электронный курс', '01'), ('Лучшее ввизуальное оформление курса', '02'), ('Лучшая инновация в контроле знаний', '03')]),
            preserve_default=True,
        ),
    ]
