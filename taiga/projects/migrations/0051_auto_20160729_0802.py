# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-29 08:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0050_project_epics_csv_uuid"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={
                "ordering": ["name", "id"],
                "verbose_name": "project",
                "verbose_name_plural": "projects",
            },
        ),
    ]
