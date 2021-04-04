from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(models.Model):
    class Meta:
        verbose_name_plural = 'company'

    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=31, blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True, help_text='Contact email')

