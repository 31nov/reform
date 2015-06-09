# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_game_game_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
