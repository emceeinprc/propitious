# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name=b'date occuring')),
                ('category', models.CharField(choices=[(b'holiday', b'Holiday'), (b'breaking_news', b'Breaking News')], max_length=200)),
            ],
        ),
    ]