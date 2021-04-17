from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField


def user_directory_path(instance, filename):
    return f'users/avatars/{instance}/{filename}'


# class User(AbstractUser):
#     is_leader = models.BooleanField(default=True)
#     is_manager = models.BooleanField(default=False)
#     phone = models.CharField(max_length=31, unique=True)
#     bio = models.TextField(max_length=510, blank=True)
#     avatar = models.ImageField(upload_to=user_directory_path, default='default.png')
#     medium_avatar = ImageSpecField(
#         source='avatar',
#         processors=[ResizeToFill(256, 256)],
#         format='JPEG',
#         options={'quality': 90}
#     )
#     small_avatar = ImageSpecField(source='avatar',
#                                   processors=[ResizeToFill(32, 32)],
#                                   format='JPEG',
#                                   options={'quality': 90})
#
#     def get_name(self):
#         return f'{self.first_name} {self.last_name}'


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        if other_fields.get('is_active') is not True:
            raise ValueError('Superuser must be assigned to is_active=True')

        return self.create_user(email, password, **other_fields)


class BasicUser(PermissionsMixin, AbstractBaseUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    is_director = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=31, unique=True)

    date_of_birth = models.DateTimeField(blank=True, null=True)
    about = models.TextField(max_length=500, blank=True)

    avatar = models.ImageField(upload_to=user_directory_path, default='default.png')
    medium_avatar = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(256, 256)],
        format='JPEG',
        options={'quality': 90}
    )
    small_avatar = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(32, 32)],
        format='JPEG',
        options={'quality': 90})

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_name(self):
        return f'{self.first_name} {self.last_name}'
