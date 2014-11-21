#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from global_permissions.models import GlobalPermission, GlobalPermissionManager


class TestGlobalPermissions(TestCase):

    def test_inherits_from_permission(self):
        self.assertTrue(isinstance(GlobalPermission(), Permission),\
                        'GlobalPermission is not an instance of Permission')

    def test_content_type_name(self):
        gp = GlobalPermission(codename='some_codename')
        gp.save()

        self.assertEquals(gp.content_type, ContentType.objects.get(name='global_permission'))
        self.assertEquals('global_permissions', gp.content_type.app_label)

    def test_default_manager_is_instance_of_global_permission_manager(self):
        self.assertTrue(isinstance(GlobalPermission.objects, GlobalPermissionManager),\
                        'GlobalPermission default manager is not an instance of '
                        'GlobalPermissionManager')

    def test_default_manager_filter_content_type_for_this_app(self):
        dummy_content_type = ContentType.objects.create(name='dummy_content_type')

        GlobalPermission.objects.create(codename='my_codename')
        Permission.objects.create(codename='my_codename', content_type=dummy_content_type)

        self.assertEquals(1, GlobalPermission.objects.count())
