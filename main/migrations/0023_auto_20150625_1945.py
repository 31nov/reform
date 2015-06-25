# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20150625_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='imgName',
            new_name='imgName1',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_image10',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_image5',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_image6',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_image7',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_image8',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_image9',
        ),
        migrations.AddField(
            model_name='article',
            name='imgName2',
            field=models.CharField(verbose_name='imgName', blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='imgName3',
            field=models.CharField(verbose_name='imgName', blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='imgName4',
            field=models.CharField(verbose_name='imgName', blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
