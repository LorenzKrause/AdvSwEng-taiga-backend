# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.apps import apps
from django.conf import settings
from django.db.models import F

from taiga.projects.notifications.services import create_notify_policy_if_not_exists


####################################
# Signals over project items
####################################

## Membership


def membership_post_delete(sender, instance, using, **kwargs):
    instance.project.update_role_points()


def membership_post_save(sender, instance, using, **kwargs):
    if not instance.user:
        return
    create_notify_policy_if_not_exists(instance.project, instance.user)

    # Set project on top on user projects list
    membership = apps.get_model("projects", "Membership")
    membership.objects.filter(user=instance.user).update(user_order=F("user_order") + 1)

    membership.objects.filter(user=instance.user, project=instance.project).update(
        user_order=0
    )


## Project attributes
def project_post_save(sender, instance, created, **kwargs):
    """
    Populate new project dependen default data
    """
    if not created:
        return

    if instance._importing:
        return

    template = getattr(instance, "creation_template", None)
    if template is None:
        ProjectTemplate = apps.get_model("projects", "ProjectTemplate")
        template = ProjectTemplate.objects.get(slug=settings.DEFAULT_PROJECT_TEMPLATE)

    if instance.tags:
        template.tags = instance.tags

    if instance.tags_colors:
        template.tags_colors = instance.tags_colors

    template.apply_to_project(instance)

    instance.save()

    Role = apps.get_model("users", "Role")
    try:
        owner_role = instance.roles.get(slug=template.default_owner_role)
    except Role.DoesNotExist:
        owner_role = instance.roles.first()

    if owner_role:
        Membership = apps.get_model("projects", "Membership")
        Membership.objects.create(
            user=instance.owner,
            project=instance,
            role=owner_role,
            is_admin=True,
            email=instance.owner.email,
        )


## US statuses


def try_to_close_or_open_user_stories_when_edit_us_status(
    sender, instance, created, **kwargs
):
    from taiga.projects.userstories import services

    for user_story in instance.user_stories.all():
        if services.calculate_userstory_is_closed(user_story):
            services.close_userstory(user_story)
        else:
            services.open_userstory(user_story)


## Task statuses


def try_to_close_or_open_user_stories_when_edit_task_status(
    sender, instance, created, **kwargs
):
    from taiga.projects.userstories import services

    UserStory = apps.get_model("userstories", "UserStory")

    for user_story in UserStory.objects.filter(tasks__status=instance).distinct():
        if services.calculate_userstory_is_closed(user_story):
            services.close_userstory(user_story)
        else:
            services.open_userstory(user_story)
