# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151212_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
