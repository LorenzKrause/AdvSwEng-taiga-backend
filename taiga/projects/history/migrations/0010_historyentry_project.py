# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-24 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0048_auto_20160615_1508"),
        ("history", "0009_auto_20160512_1110"),
    ]

    operations = [
        migrations.AddField(
            model_name="historyentry",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.Project",
            ),
        ),
    ]
