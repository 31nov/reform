# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_article_imgname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='file_image',
            new_name='file_image1',
        ),
        migrations.AddField(
            model_name='article',
            name='file_image10',
            field=models.ImageField(verbose_name='이미지:', upload_to='img/%Y/%m', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_image2',
            field=models.ImageField(verbose_name='이미지:', upload_to='img/%Y/%m', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_image3',
            field=models.ImageField(verbose_name='이미지:', upload_to='img/%Y/%m', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_image4',
            field=models.ImageField(verbose_name='이미지:', upload_to='img/%Y/%m', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_image5',
            field=models.ImageField(verbose_name='이미지:', upload_to='img/%Y/%m', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_image6',
            field=models.ImageField(verbose_name='이미지:', upload_to='img/%Y/%m', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_image7',
            field=models.ImageField(verbose_name='이미지:', upload_to='img/%Y/%m', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_image8',
            field=models.ImageField(verbose_name='이미지:', upload_to='img/%Y/%m', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='file_image9',
            field=models.ImageField(verbose_name='이미지:', upload_to='img/%Y/%m', blank=True),
            preserve_default=True,
        ),
    ]
