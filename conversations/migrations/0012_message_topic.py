# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0011_auto_20151209_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='topic',
            field=models.CharField(default=b'', max_length=300, verbose_name=b'conversation topic'),
        ),
    ]
