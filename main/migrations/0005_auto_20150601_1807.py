# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_article_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='글 제목', max_length=200)),
                ('content1', models.TextField(verbose_name='글 내용1')),
                ('content2', models.TextField(verbose_name='글 내용2')),
                ('content3', models.TextField(verbose_name='글 내용3')),
                ('content4', models.TextField(verbose_name='글 내용4')),
                ('written_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='글 내용'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(verbose_name='글 제목', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.TextField(verbose_name='댓글 내용'),
            preserve_default=True,
        ),
    ]
