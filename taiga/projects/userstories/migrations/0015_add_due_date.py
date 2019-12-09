# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-09 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userstories", "0014_auto_20160928_0540"),
    ]

    operations = [
        migrations.AddField(
            model_name="userstory",
            name="due_date",
            field=models.DateField(
                blank=True, default=None, null=True, verbose_name="due date"
            ),
        ),
        migrations.AddField(
            model_name="userstory",
            name="due_date_reason",
            field=models.TextField(
                blank=True, default="", verbose_name="reason for the due date"
            ),
        ),
    ]
