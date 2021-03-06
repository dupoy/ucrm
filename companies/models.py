from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import reverse_lazy
from django.utils.text import slugify

User = get_user_model()


class Company(models.Model):
    class Meta:
        verbose_name_plural = 'companies'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=31, help_text='Contact phone number')
    email = models.EmailField(help_text='Contact email')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('companies:dashboard', args=[self.slug])

    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Company)
def delete_company(sender, instance, **kwargs):
    for manager in instance.managers.all():
        user = User.objects.filter(manager=manager).first()
        user.delete()
