# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 06:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("timeline", "0006_json_to_jsonb"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="timeline",
            index_together=set(
                [("content_type", "object_id", "namespace"), ("namespace", "created")]
            ),
        ),
    ]
