# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(default='', max_length=2500),
        ),
    ]