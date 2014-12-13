# -*- coding: utf-8 -*-

import django
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _


class GlobalPermissionManager(models.Manager):
    def get_queryset(self):
        return super(GlobalPermissionManager, self).get_query_set().\
            filter(content_type__name='global_permission')


if django.VERSION < (1, 6,):
    GlobalPermissionManager.get_query_set =\
        GlobalPermissionManager.get_queryset


class GlobalPermission(Permission):
    """A global permission, not attached to a model"""

    objects = GlobalPermissionManager()

    class Meta:
        proxy = True
        verbose_name = _('Global Permission')
        verbose_name_plural = _('Global Permissions')

    def save(self, *args, **kwargs):
        ct, created = ContentType.objects.get_or_create(
            name='global_permission', app_label=self._meta.app_label,
            model='globalpermission'
        )

        self.content_type = ct
        super(GlobalPermission, self).save(*args, **kwargs)
