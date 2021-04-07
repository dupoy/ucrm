from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField


def user_directory_path(instance, filename):
    return f'users/avatars/{instance}/{filename}'


class User(AbstractUser):
    is_leader = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    phone = models.CharField(max_length=31, unique=True)
    bio = models.TextField(max_length=510, blank=True)
    avatar = models.ImageField(upload_to=user_directory_path, default='default.png')
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(32, 32)],
                                      format='JPEG',
                                      options={'quality': 90})

    def get_name(self):
        return f'{self.first_name} {self.last_name}'
