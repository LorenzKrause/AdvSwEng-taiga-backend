# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 11:35
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ("webhooks", "0005_auto_20150505_1639"),
    ]

    operations = [
        migrations.RunSQL(
            """
                ALTER TABLE "webhooks_webhooklog"
                   ALTER COLUMN "request_headers"
                           TYPE jsonb
                          USING regexp_replace("request_headers"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "request_data"
                           TYPE jsonb
                          USING regexp_replace("request_data"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "response_headers"
                           TYPE jsonb
                          USING regexp_replace("response_headers"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
