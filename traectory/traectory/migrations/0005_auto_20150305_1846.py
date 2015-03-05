# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traectory', '0004_cell_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='coment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='traectory',
            old_name='coment',
            new_name='comment',
        ),
    ]
