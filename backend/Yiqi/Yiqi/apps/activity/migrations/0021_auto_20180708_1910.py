# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-08 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0020_auto_20180707_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityimagesmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ActivityImagesModel/%y/%d/ea83c307f8a142e195e2709fd2900965', verbose_name='活动图片'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='Activity/%y/%d/ea83c307f8a142e195e2709fd2900965', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='groupcode',
            field=models.ImageField(blank=True, null=True, upload_to='Activity/qr/%y/%d/ea83c307f8a142e195e2709fd2900965', verbose_name='群二维码'),
        ),
        migrations.AlterField(
            model_name='activitytypemodel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='ActivityTypeModel/%y/%d/ea83c307f8a142e195e2709fd2900965', verbose_name='类别图片'),
        ),
        migrations.AlterField(
            model_name='slidemodels',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='SlideModels/%y/%d/ea83c307f8a142e195e2709fd2900965', verbose_name='幻灯片图片'),
        ),
    ]