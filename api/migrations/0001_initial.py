# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
        ),
    ]
