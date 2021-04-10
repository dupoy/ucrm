from django.contrib import admin

# Register your models here.
from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
