# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversations', '0009_auto_20151204_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='parent',
            field=models.ForeignKey(related_name='children', to='conversations.Message', null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='root',
            field=models.ForeignKey(related_query_name=b'children_of', related_name='decendents', to='conversations.Message', null=True),
        ),
    ]
