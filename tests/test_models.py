#!/usr/bin/env python
# -*- coding: utf-8 -*-

import django
from django.test import TestCase
from django.db.models import Q
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from global_permissions.models import GlobalPermission, GlobalPermissionManager


class TestGlobalPermissions(TestCase):
    def setUp(self):
        # for some reason the entries are not being deleted
        # between tests
        ContentType.objects.all().delete()

    def test_inherits_from_permission(self):
        self.assertTrue(isinstance(GlobalPermission(), Permission),\
                        'GlobalPermission is not an instance of Permission')

    def test_content_type_name(self):
        gp = GlobalPermission(codename='some_codename')
        gp.save()

        self.assertEquals('global_permissions', gp.content_type.app_label)

        lookup = Q(model='globalpermission', app_label='global_permissions')
        if django.VERSION < (1, 8):
            lookup &= Q(name='global_permission')

        self.assertEquals(gp.content_type, ContentType.objects.get(lookup))

    def test_default_manager_is_instance_of_global_permission_manager(self):
        self.assertTrue(isinstance(GlobalPermission.objects, GlobalPermissionManager),\
                        'GlobalPermission default manager is not an instance of '
                        'GlobalPermissionManager')

    def test_default_manager_filter_content_type_for_this_app(self):
        dummy_content_type = ContentType.objects.create(name='dummy_content_type')

        GlobalPermission.objects.create(codename='my_codename')
        Permission.objects.create(codename='my_codename', content_type=dummy_content_type)

        self.assertEquals(1, GlobalPermission.objects.count())
