# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('UserManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]