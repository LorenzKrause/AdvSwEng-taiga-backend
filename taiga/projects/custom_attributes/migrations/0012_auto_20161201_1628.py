# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("custom_attributes", "0011_json_to_jsonb"),
    ]

    operations = [
        migrations.AlterField(
            model_name="epiccustomattribute",
            name="type",
            field=models.CharField(
                choices=[
                    ("text", "Text"),
                    ("multiline", "Multi-Line Text"),
                    ("richtext", "Rich text"),
                    ("date", "Date"),
                    ("url", "Url"),
                ],
                default="text",
                max_length=16,
                verbose_name="type",
            ),
        ),
        migrations.AlterField(
            model_name="issuecustomattribute",
            name="type",
            field=models.CharField(
                choices=[
                    ("text", "Text"),
                    ("multiline", "Multi-Line Text"),
                    ("richtext", "Rich text"),
                    ("date", "Date"),
                    ("url", "Url"),
                ],
                default="text",
                max_length=16,
                verbose_name="type",
            ),
        ),
        migrations.AlterField(
            model_name="taskcustomattribute",
            name="type",
            field=models.CharField(
                choices=[
                    ("text", "Text"),
                    ("multiline", "Multi-Line Text"),
                    ("richtext", "Rich text"),
                    ("date", "Date"),
                    ("url", "Url"),
                ],
                default="text",
                max_length=16,
                verbose_name="type",
            ),
        ),
        migrations.AlterField(
            model_name="userstorycustomattribute",
            name="type",
            field=models.CharField(
                choices=[
                    ("text", "Text"),
                    ("multiline", "Multi-Line Text"),
                    ("richtext", "Rich text"),
                    ("date", "Date"),
                    ("url", "Url"),
                ],
                default="text",
                max_length=16,
                verbose_name="type",
            ),
        ),
    ]
