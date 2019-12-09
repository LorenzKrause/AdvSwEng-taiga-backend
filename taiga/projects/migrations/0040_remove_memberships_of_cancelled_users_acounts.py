# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 15:46
from __future__ import unicode_literals

from django.db import migrations


def remove_memberships_of_cancelled_users_acounts(apps, schema_editor):
    Membership = apps.get_model("projects", "Membership")
    Membership.objects.filter(user__is_active=False).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0039_auto_20160322_1157"),
    ]

    operations = [
        migrations.RunPython(remove_memberships_of_cancelled_users_acounts),
    ]
