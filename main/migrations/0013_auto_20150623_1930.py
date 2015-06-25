# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150622_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='file_image',
            field=models.ImageField(verbose_name='이미지:', null=True, upload_to='img/%Y/%m', blank=True),
            preserve_default=True,
        ),
    ]
