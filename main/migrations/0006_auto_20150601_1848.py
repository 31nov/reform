# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150601_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='user',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.AddField(
            model_name='article',
            name='file_game_mac',
            field=models.FileField(verbose_name='게임 -> MAC :', blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_game_apk',
            field=models.FileField(verbose_name='게임 -> AOS :', blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_game_exe',
            field=models.FileField(verbose_name='게임 -> EXE :', blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_game_ios',
            field=models.FileField(verbose_name='게임 -> IOS :', blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_image',
            field=models.FileField(verbose_name='이미지:', upload_to='', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='file_image',
            field=models.FileField(verbose_name='이미지:', blank=True, upload_to=''),
            preserve_default=True,
        ),
    ]
