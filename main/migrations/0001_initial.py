# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('userId', models.CharField(max_length=100, verbose_name='User ID Enter')),
                ('userPW', models.CharField(max_length=100, verbose_name='User Password Enter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
