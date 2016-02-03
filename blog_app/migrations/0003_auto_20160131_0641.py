# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('heading', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog_app.blog_post'),
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]
