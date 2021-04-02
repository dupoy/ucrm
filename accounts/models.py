from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from phone_field import PhoneField


class User(AbstractUser):
    is_leader = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    phone = PhoneField(blank=False, help_text='Contact phone number')
