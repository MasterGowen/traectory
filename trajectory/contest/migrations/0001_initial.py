# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('route', models.CharField(verbose_name='Направление', max_length=2, choices=[('01', '01'), ('02', '02'), ('03', '03')])),
                ('organization', models.CharField(verbose_name='Организация', max_length=1024)),
                ('city', models.CharField(verbose_name='Город', max_length=1024)),
                ('authors', models.CharField(verbose_name='Авторы', max_length=1024)),
                ('email', models.EmailField(verbose_name='Электронная почта', max_length=1024)),
                ('telephone', models.CharField(verbose_name='Контактный телефон', max_length=1024)),
                ('url', models.URLField(max_length=1024, verbose_name='Адрес ресурса', null=True, blank=True)),
                ('account', models.CharField(max_length=1024, verbose_name='Реквизиты доступа', null=True, blank=True)),
                ('description', models.CharField(verbose_name='Описание основных идей', max_length=4096)),
                ('summary_rank', models.IntegerField(max_length=8, verbose_name='Общая оценка', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContestItemRank',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('user_rank', models.IntegerField(max_length=8, verbose_name='Оценка', null=True, blank=True)),
                ('user_comment', models.CharField(max_length=4096, verbose_name='Комментарий', null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contestitem',
            name='rank',
            field=models.ManyToManyField(to='contest.ContestItemRank'),
            preserve_default=True,
        ),
    ]
