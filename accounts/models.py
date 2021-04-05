from io import BytesIO
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.db import models
from django.db.models import ForeignKey


def user_directory_path(instance, filename):
    return f'users/avatars/{instance}/{filename}'


def compress_image(image):
    im = Image.open(image)
    im_io = BytesIO()
    rgb_im = im.convert('RGB')
    rgb_im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


class User(AbstractUser):
    is_leader = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    phone = models.CharField(max_length=31, unique=True)
    bio = models.TextField(max_length=510, blank=True)
    avatar = models.ImageField(upload_to=user_directory_path, default='default.png')

    def save(self, **kwargs):
        if not self.id:
            self.image = compress_image(self.avatar)
        super(User, self).save()

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

