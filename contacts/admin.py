from django.contrib import admin
from contacts.models import Contact, ContactHistory


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactHistory)
class ContactHistoryAdmin(admin.ModelAdmin):
    pass
