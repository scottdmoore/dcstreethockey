# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-28 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0046_auto_20171227_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='alt_announcement1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='alt_announcement2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='alt_photo1',
            field=models.ImageField(blank=True, null=True, upload_to='homepage'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='alt_photo2',
            field=models.ImageField(blank=True, null=True, upload_to='homepage'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='alt_title1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='alt_title2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]