# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20150624_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, verbose_name='글 내용', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_image',
            field=models.ImageField(blank=True, verbose_name='이미지:', upload_to='img/%Y/%m'),
            preserve_default=True,
        ),
    ]
