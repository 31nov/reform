# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150601_2301'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name_plural': '프로필', 'verbose_name': '프로필'},
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_photo',
        ),
        migrations.AddField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(verbose_name='댓글 수 ', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='like_count',
            field=models.IntegerField(verbose_name='좋아요 수', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='pic',
            field=models.FileField(blank=True, upload_to='', verbose_name='사진'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_game_apk',
            field=models.FileField(blank=True, verbose_name='게임 -> AOS :', upload_to='', default='X'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_game_exe',
            field=models.FileField(blank=True, verbose_name='게임 -> EXE :', upload_to='', default='X'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_game_ios',
            field=models.FileField(blank=True, verbose_name='게임 -> IOS :', upload_to='', default='X'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_game_mac',
            field=models.FileField(blank=True, verbose_name='게임 -> MAC :', upload_to='', default='X'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_image',
            field=models.FileField(blank=True, verbose_name='이미지:', upload_to='', default='X'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
