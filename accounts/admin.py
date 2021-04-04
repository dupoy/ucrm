from django.contrib import admin

# Register your models here.
from accounts.models import User


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
