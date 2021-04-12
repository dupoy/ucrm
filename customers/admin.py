from django.contrib import admin

# Register your models here.
from customers.models import Customer, Contact


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass