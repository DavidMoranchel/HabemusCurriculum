# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-10 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField()),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Skills')),
            ],
        ),
    ]
