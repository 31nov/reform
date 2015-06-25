# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_article_imgname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='imgName',
        ),
    ]
