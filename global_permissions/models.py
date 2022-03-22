# -*- coding: utf-8 -*-

import django
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

try:
    from django.utils.translation import gettext_lazy as _
except ImportError:
    from django.utils.translation import ugettext_lazy as _


class GlobalPermissionManager(models.Manager):
    use_in_migrations = True

    if django.VERSION < (1, 6,):
        def get_query_set(self):
            return super(GlobalPermissionManager, self).get_query_set().\
                filter(content_type__name='global_permission')
    elif django.VERSION < (1, 8,):
        def get_queryset(self):
            return super(GlobalPermissionManager, self).get_queryset().\
                filter(content_type__name='global_permission')
    else:
        def get_queryset(self):
            return super(GlobalPermissionManager, self).get_queryset().\
                filter(content_type__model='globalpermission')


class GlobalPermission(Permission):
    """A global permission, not attached to a model"""

    objects = GlobalPermissionManager()

    class Meta:
        proxy = True
        verbose_name = _('Global Permission')
        verbose_name_plural = _('Global Permissions')

    def save(self, *args, **kwargs):
        content_type_kwargs = {'app_label': self._meta.app_label,
                               'model': 'globalpermission'}
        if django.VERSION < (1, 8):
            content_type_kwargs['name'] = 'global_permission'
        ct, created = ContentType.objects.get_or_create(**content_type_kwargs)

        self.content_type = ct
        super(GlobalPermission, self).save(*args, **kwargs)
