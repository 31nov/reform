# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20150513_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='글 제목 : ')),
                ('content', models.TextField(verbose_name='글 내용 : ')),
                ('written_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('file_image', models.FileField(verbose_name='이미지:', upload_to='')),
                ('file_game_apk', models.FileField(verbose_name='게임 -> AOS :', upload_to='')),
                ('file_game_ios', models.FileField(verbose_name='게임 -> IOS :', upload_to='')),
                ('file_game_exe', models.FileField(verbose_name='게임 -> EXE :', upload_to='')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='댓글 내용 :')),
                ('written_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('file_image', models.FileField(verbose_name='이미지:', upload_to='')),
                ('article', models.ForeignKey(to='main.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
