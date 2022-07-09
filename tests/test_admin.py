
import platform
from django.test import TestCase

if platform.python_version() >= '3.8':
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User


class GlobalPermissionsAdminTest(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='ham', password='spam', email='ham@spam.com')
        self.client.login(username='ham', password='spam')

    def test_admin_simply_works(self):
        resp = self.client.get(reverse('admin:global_permissions_globalpermission_changelist'))
        self.assertEqual(200, resp.status_code)
