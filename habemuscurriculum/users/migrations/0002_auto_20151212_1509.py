# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
