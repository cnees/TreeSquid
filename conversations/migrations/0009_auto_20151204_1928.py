# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0008_message_root'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='root',
            field=models.ForeignKey(related_query_name=b'children', related_name='children_of', to='conversations.Message', null=True),
        ),
    ]
