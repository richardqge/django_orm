# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-26 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20191126_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='the_book',
            new_name='book',
        ),
    ]
