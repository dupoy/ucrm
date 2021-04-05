from django.contrib import admin
from company.models import Company, Manager


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass
