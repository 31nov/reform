# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150623_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='article',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_game_apk',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_game_exe',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_game_ios',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_game_mac',
        ),
        migrations.RemoveField(
            model_name='article',
            name='like_count',
        ),
    ]
