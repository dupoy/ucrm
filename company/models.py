from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy

User = get_user_model()


class Company(models.Model):
    class Meta:
        verbose_name_plural = 'company'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=31, blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True, help_text='Contact email')

    def get_absolute_url(self):
        return reverse_lazy('company:detail', args=[self.pk])
