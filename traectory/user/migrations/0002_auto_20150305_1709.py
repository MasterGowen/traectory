# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(verbose_name='Город', max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(verbose_name='Электронная почта', max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='f',
            field=models.CharField(verbose_name='Фамилия', max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='i',
            field=models.CharField(verbose_name='Имя', max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='o',
            field=models.CharField(verbose_name='Отчество', max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('online', 'Заочно'), ('offline', 'Очно')], verbose_name='Статус', default='offline', max_length=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(verbose_name='Телефон', max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('email', 'f')]),
        ),
    ]
