from django.contrib import admin

# Register your models here.
# from accounts.models import User, BasicUser
from accounts.models import BasicUser


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'first_name', 'last_name', 'email', 'phone']


@admin.register(BasicUser)
class BasicUserAdmin(admin.ModelAdmin):
    list_display_links = ['email']
    list_display = ['email', 'first_name', 'last_name', 'phone', 'is_director', 'is_manager']
