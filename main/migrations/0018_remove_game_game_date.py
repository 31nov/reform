# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20150608_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_date',
        ),
    ]
