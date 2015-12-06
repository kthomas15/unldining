# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meal_date', models.DateField()),
                ('breakfast', models.IntegerField(null=True, blank=True)),
                ('lunch', models.IntegerField(null=True, blank=True)),
                ('dinner', models.IntegerField(null=True, blank=True)),
                ('late_night', models.IntegerField(null=True, blank=True)),
                ('total', models.IntegerField(null=True, blank=True)),
                ('hall', models.ForeignKey(to='dininghall.Hall')),
            ],
        ),
    ]
