# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-21 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_user_adminify'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
