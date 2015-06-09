# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150602_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='userInfo',
            field=models.ForeignKey(to='main.UserInfo', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pic',
            field=models.FileField(verbose_name='사진', upload_to='', default='media/user/emptyIser.png', blank=True),
            preserve_default=True,
        ),
    ]
