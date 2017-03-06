from django.conf.urls import include, url

try:
    from django.conf.urls import patterns
except ImportError:
    patterns = lambda _, *endpoints: endpoints

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
