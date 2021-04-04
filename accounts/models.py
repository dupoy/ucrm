from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_leader = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
