# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150603_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('game', models.CharField(verbose_name='title ', max_length=200)),
                ('gameImage', models.CharField(verbose_name='img ', max_length=300)),
                ('gameComment', models.CharField(verbose_name='comment 수 ', max_length=400, default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
