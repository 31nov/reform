# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150601_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='file_image',
            field=models.FileField(verbose_name='이미지:', upload_to='', blank=True),
            preserve_default=True,
        ),
    ]
