# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('user_nickname', models.TextField()),
                ('user_score', models.BigIntegerField()),
                ('user_signin_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('connect_time', models.DateTimeField(blank=True, null=True)),
                ('shutgame_time', models.DateTimeField(blank=True, null=True)),
                ('lastplay_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
