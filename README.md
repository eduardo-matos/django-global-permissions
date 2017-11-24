# Django Global Permissions

[![Build Status](https://travis-ci.org/eduardo-matos/django-global-permissions.svg?branch=master)](https://travis-ci.org/eduardo-matos/django-global-permissions)

Implementation of permissions not related to models

# Quickstart

Install django-global-permissions:

```
pip install django-global-permissions
```

Add to installed apps:

```python
INSTALLED_APPS += ('global_permissions',)
```

If you want to create a permission in the admin interface, then head to
the Global Permissions section and click _add_. Pick a name (which should be
human readable), a code name (which will be used throughout your apps), then save it.
Open the user edit page and choose the permission you've just created.

![](https://user-images.githubusercontent.com/483681/33212448-58a39f36-d10a-11e7-88c9-332df034188c.gif)

Otherwise if you want to create a permission programmatically, just import the `GlobalPermission`
model and create a new permission choosing a name and a codename.

```python
from global_permissions.models import GlobalPermission

GlobalPermission.objects.create(name='My Perm', codename='my_perm')
```

## Putting into action!

Lets say you want to verify if the logged in user can do something (based on a permission).
In your view, you can do the following

```python
if user.has_perm('global_permissions.my_perm_codename'):
    pass # do something intersting!
else:
    pass # ops, you're not allowed to do that. Sorry ¯\_(ツ)_/¯
```

If you want to check a permission in a template, you can do it like this:

```htmldjango
{% if perms.global_permissions.my_perm_codename %}
    Yay!
{% else %}
    Not so lucky...
{% endif %}
```

## Upgrade

If you're upgrading from version 0.1.x to version 0.2.x, you have to manually update the old contentttype model attribute to the new one. The following script may do the trick:

```python
from django.contrib.contenttypes.models import ContentType

ContentType.objects.filter(name='global_permission', app_label='global_permissions').update(model='globalpermission')
```

This change is required on django 1.7+ to avoid a prompt asking if you want to remove staled content types after running a migration.
