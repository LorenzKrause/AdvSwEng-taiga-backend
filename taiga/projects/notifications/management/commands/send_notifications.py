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


from django.core.management.base import BaseCommand

from taiga.base.utils.iterators import iter_queryset
from taiga.projects.notifications.models import HistoryChangeNotification
from taiga.projects.notifications.services import send_sync_notifications

from django_pglocks import advisory_lock


class Command(BaseCommand):
    def handle(self, *args, **options):
        with advisory_lock("send-notifications-command", wait=False) as acquired:
            if acquired:
                qs = HistoryChangeNotification.objects.all()
                for change_notification in iter_queryset(qs, itersize=100):
                    try:
                        send_sync_notifications(change_notification.pk)
                    except HistoryChangeNotification.DoesNotExist:
                        pass
            else:
                print("Other process already running")
