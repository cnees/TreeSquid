# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0004_auto_20151203_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='parent',
            field=models.ForeignKey(default=0, to='conversations.Message'),
        ),
    ]
