from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_leader = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    phone = models.CharField(max_length=31, blank=False, help_text='Contact phone number')
