#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-global-permissions
------------

Tests for `django-global-permissions` models module.
"""

import os
import shutil
import unittest

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from global_permissions.models import GlobalPermission, GlobalPermissionManager


class TestGlobalPermissions(unittest.TestCase):

    def test_inherits_from_permission(self):
        self.assertIsInstance(GlobalPermission(), Permission)

    def test_content_type_name(self):
        gp = GlobalPermission(codename='some_codename')
        gp.save()

        self.assertEquals(gp.content_type, ContentType.objects.get(name='global_permission'))
        self.assertEquals('global_permissions', gp.content_type.app_label)

    def test_default_manager_is_instance_of_global_permission_manager(self):
        self.assertIsInstance(GlobalPermission.objects, GlobalPermissionManager)

    def test_default_manager_filter_content_type_for_this_app(self):
        dummy_content_type = ContentType.objects.create(name='dummy_content_type')

        GlobalPermission.objects.create(codename='my_codename')
        Permission.objects.create(codename='my_codename', content_type=dummy_content_type)

        self.assertEquals(1, GlobalPermission.objects.count())

    def tearDown(self):
        Permission.objects.all().delete()
        GlobalPermission.objects.all().delete()
        ContentType.objects.all().delete()
