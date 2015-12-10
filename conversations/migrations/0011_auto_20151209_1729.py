# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0010_auto_20151204_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='root',
            field=models.ForeignKey(related_query_name=b'children_of', related_name='descendants', to='conversations.Message', null=True),
        ),
    ]
