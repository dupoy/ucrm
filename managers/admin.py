from django.contrib import admin

from managers.models import Manager


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass
