from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from django.urls import reverse_lazy

User = get_user_model()


class Company(models.Model):
    class Meta:
        verbose_name_plural = 'company'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=31, blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True, help_text='Contact email')

    def get_absolute_url(self):
        return reverse_lazy('company:detail', args=[self.pk])

    def __str__(self):
        return self.name


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='managers')

    def __str__(self):
        return self.user.username


@receiver(pre_delete, sender=Company)
def delete_user(sender, instance, **kwargs):
    managers = Manager.objects.filter(company=instance)
    for manager in managers:
        user = User.objects.filter(manager=manager).first()
        user.delete()
