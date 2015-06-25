# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20150625_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='file_image1',
            new_name='file_image',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='imgName1',
            new_name='imgName',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_image2',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_image3',
        ),
        migrations.RemoveField(
            model_name='article',
            name='file_image4',
        ),
        migrations.RemoveField(
            model_name='article',
            name='imgName2',
        ),
        migrations.RemoveField(
            model_name='article',
            name='imgName3',
        ),
        migrations.RemoveField(
            model_name='article',
            name='imgName4',
        ),
    ]
