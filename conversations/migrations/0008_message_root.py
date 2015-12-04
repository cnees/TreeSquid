# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0007_auto_20151203_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='root',
            field=models.ForeignKey(related_name='child_of', to='conversations.Message', null=True),
        ),
    ]
