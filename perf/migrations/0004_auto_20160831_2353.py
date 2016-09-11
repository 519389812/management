# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-31 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0003_auto_20160829_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='\u59d3\u540d')),
                ('team', models.CharField(choices=[('\u4e00\u5ba4', '\u4e00\u5ba4'), ('\u4e8c\u5ba4', '\u4e8c\u5ba4'), ('\u4e09\u5ba4', '\u4e09\u5ba4'), ('\u56e2\u961f', '\u56e2\u961f')], max_length=4, verbose_name='\u5ba4\u522b')),
                ('year', models.IntegerField(max_length=4, verbose_name='\u5e74\u4efd')),
                ('month', models.IntegerField(max_length=4, verbose_name='\u6708\u4efd')),
                ('workload', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u4eba\u6570')),
                ('point', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u52a0\u5206')),
            ],
            options={
                'verbose_name': '\u6458\u8981',
                'verbose_name_plural': '\u7ee9\u6548\u7edf\u8ba1',
            },
        ),
        migrations.AlterField(
            model_name='add',
            name='point',
            field=models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u52a0\u5206'),
        ),
        migrations.AlterField(
            model_name='add',
            name='values',
            field=models.FloatField(max_length=4, verbose_name='\u6570\u503c'),
        ),
        migrations.AlterField(
            model_name='add',
            name='verify',
            field=models.BooleanField(default=False, verbose_name='\u5ba1\u6838\u72b6\u6001'),
        ),
    ]
