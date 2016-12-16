# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherManage', '0003_vip'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='academy',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='education',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='academy',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tag',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]