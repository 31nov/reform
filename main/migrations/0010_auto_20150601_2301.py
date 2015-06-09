# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150601_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_photo',
            field=models.FileField(upload_to='', default='/static/image/emptyUser.png'),
            preserve_default=True,
        ),
    ]
