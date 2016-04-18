# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cube',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('image', models.CharField(max_length=250)),
                ('is_custom', models.BooleanField(default=False)),
                ('slug', models.SlugField(unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
