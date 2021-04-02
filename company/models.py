from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True, help_text='Contact email')
