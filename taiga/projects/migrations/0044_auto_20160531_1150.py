# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0043_auto_20160530_1004"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="blocked_code",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "blocked-by-nonpayment",
                        "This project is blocked due to payment failure",
                    ),
                    ("blocked-by-staff", "This project is blocked by admin staff"),
                    (
                        "blocked-by-owner-leaving",
                        "This project is blocked because the owner left",
                    ),
                    (
                        "blocked-by-deleting",
                        "This project is blocked while it's deleted",
                    ),
                ],
                default=None,
                max_length=255,
                null=True,
                verbose_name="blocked code",
            ),
        ),
    ]
