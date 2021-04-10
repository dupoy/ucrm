from django.contrib import admin
from companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    prepopulated_fields = {'slug': ('name',), }
