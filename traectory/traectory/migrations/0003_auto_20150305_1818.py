# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20150305_1750'),
        ('traectory', '0002_auto_20150305_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='events',
            field=models.ManyToManyField(to='event.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='program',
            name='cells',
            field=models.ManyToManyField(to='traectory.Cell'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='program',
            name='coment',
            field=models.TextField(max_length=4096, null=True, blank=True, verbose_name='Описание'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='program',
            name='name',
            field=models.CharField(max_length=1024, null=True, blank=True, verbose_name='Название'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='program',
            name='payd',
            field=models.BooleanField(default=False, verbose_name='Платно'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='traectory',
            name='coment',
            field=models.CharField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='traectory',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, default='None', max_length=32),
            preserve_default=True,
        ),
    ]
