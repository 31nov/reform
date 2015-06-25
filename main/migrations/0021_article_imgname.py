# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_article_imgname'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imgName',
            field=models.CharField(verbose_name='imgName', blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
