
import platform

from django.contrib import admin
admin.autodiscover()

if platform.python_version() >= '3.8':
    from django.urls import re_path
    
    urlpatterns = [
        re_path(r'^admin/', admin.site.urls),
    ]
    
else:
    from django.conf.urls import include, url

    try:
        from django.conf.urls import patterns
    except ImportError:
        patterns = lambda _, *endpoints: endpoints

    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
    )
