from django.contrib import admin
from .models import GlobalPermission


class GlobalPermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename',)
    fields = ('name', 'codename',)


admin.site.register(GlobalPermission, GlobalPermissionAdmin)
