# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherManage', '0005_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='topic',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
