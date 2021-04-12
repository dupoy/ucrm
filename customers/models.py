from django.db import models
from django.urls import reverse_lazy
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from companies.models import Company
from managers.models import Manager


def user_directory_path(instance, filename):
    return f'customers/avatars/{instance}/{filename}'


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    note = models.TextField(max_length=500, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
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
        options={'quality': 90}
    )

    def get_absolute_url(self):
        return reverse_lazy('customers:detail', args=[self.company.slug, self.pk])

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_name()
