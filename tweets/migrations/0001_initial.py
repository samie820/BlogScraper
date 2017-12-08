# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-08 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tweets', models.TextField(blank=True, null=True)),
                ('positive_remark', models.CharField(blank=True, max_length=200, null=True)),
                ('negative_remark', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
