# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_auto_20150624_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nick', models.CharField(verbose_name='별명', blank=True, max_length=50)),
                ('pic', models.ImageField(verbose_name='사진', upload_to='user', default='emptyUser.png', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '프로필',
                'verbose_name_plural': '프로필',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(verbose_name='댓글 수 ', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_game_apk',
            field=models.FileField(verbose_name='게임 -> AOS :', upload_to='', default='X', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_game_exe',
            field=models.FileField(verbose_name='게임 -> EXE :', upload_to='', default='X', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_game_ios',
            field=models.FileField(verbose_name='게임 -> IOS :', upload_to='', default='X', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_game_mac',
            field=models.FileField(verbose_name='게임 -> MAC :', upload_to='', default='X', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='like_count',
            field=models.IntegerField(verbose_name='좋아요 수', default=0),
            preserve_default=True,
        ),
    ]
