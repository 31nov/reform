# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20150625_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imgName',
            field=models.CharField(max_length=200, default=1, verbose_name='imgName'),
            preserve_default=False,
        ),
    ]
