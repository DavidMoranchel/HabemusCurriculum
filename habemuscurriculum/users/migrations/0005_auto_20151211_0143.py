# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 01:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151210_1619'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Skill_User',
        ),
    ]