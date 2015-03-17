# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trajectory', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('i', models.CharField(verbose_name='Имя', max_length=1024)),
                ('f', models.CharField(verbose_name='Фамилия', max_length=1024)),
                ('o', models.CharField(verbose_name='Отчество', max_length=1024)),
                ('city', models.CharField(verbose_name='Город', max_length=1024)),
                ('email', models.EmailField(verbose_name='Электронная почта', max_length=1024)),
                ('tel', models.CharField(verbose_name='Телефон', max_length=1024)),
                ('link', models.CharField(verbose_name='Персональная ссылка', max_length=1024)),
                ('status', models.CharField(choices=[('online', 'Заочно'), ('offline', 'Очно')], default='offline', verbose_name='Статус', max_length=7)),
                ('date', models.DateField(auto_now_add=True)),
                ('trajectories', models.ManyToManyField(to='trajectory.Trajectory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('email', 'f')]),
        ),
    ]
