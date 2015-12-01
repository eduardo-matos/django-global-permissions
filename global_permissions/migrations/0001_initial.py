# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalPermission',
            fields=[
            ],
            options={
                'verbose_name': 'Global Permission',
                'proxy': True,
                'verbose_name_plural': 'Global Permissions',
            },
            bases=('auth.permission',),
        ),
    ]
