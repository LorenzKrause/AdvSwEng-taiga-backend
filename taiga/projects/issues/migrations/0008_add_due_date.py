# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-09 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("issues", "0007_auto_20160614_1201"),
    ]

    operations = [
        migrations.AddField(
            model_name="issue",
            name="due_date",
            field=models.DateField(
                blank=True, default=None, null=True, verbose_name="due date"
            ),
        ),
        migrations.AddField(
            model_name="issue",
            name="due_date_reason",
            field=models.TextField(
                blank=True, default="", verbose_name="reason for the due date"
            ),
        ),
    ]
