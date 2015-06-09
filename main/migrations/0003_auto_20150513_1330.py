# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150513_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='GameTitle',
            new_name='gameTitle',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='Gameimage',
            new_name='gameimage',
        ),
    ]
