# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=5000, verbose_name=b'message text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name=b'last modified')),
                ('parent', models.ForeignKey(to='conversations.Message')),
            ],
        ),
    ]
