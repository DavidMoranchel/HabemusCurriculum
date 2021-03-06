# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 03:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('facebook', models.CharField(max_length=50, null=True)),
                ('twitter', models.CharField(max_length=50, null=True)),
                ('github', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to=users.models.skill_directory_path)),
            ],
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='skills',
            field=models.ManyToManyField(to='users.Skill'),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
