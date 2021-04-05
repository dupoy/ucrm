import sys
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def user_directory_path(instance, filename):
    return f'users/avatars/{instance}/{filename}'


def compress_image(image):
    image_temporary = Image.open(image)
    output_io_stream = BytesIO()
    image_temporary.save(output_io_stream, format='JPEG', quality=60)
    output_io_stream.seek(0)
    uploaded_image = InMemoryUploadedFile(
        output_io_stream, 'ImageField', "%s.jpg" % image.name.split('.')[0],
        'image/jpeg', sys.getsizeof(output_io_stream), None
    )
    return uploaded_image


class User(AbstractUser):
    is_leader = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=31, blank=True, unique=True)
    bio = models.TextField(max_length=510, blank=True)
    avatar = models.ImageField(upload_to=user_directory_path, default='default.png')

    def __str__(self):
        return self.user.username

    def save(self, **kwargs):
        if not self.id:
            self.image = compress_image(self.image)
        super(Profile, self).save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
