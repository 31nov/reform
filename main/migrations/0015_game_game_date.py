# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_date',
            field=models.DateTimeField(auto_now_add=True, default=2),
            preserve_default=False,
        ),
    ]
