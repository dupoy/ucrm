from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models
from customers.models import Customer

User = get_user_model()


class ContactType(models.TextChoices):
    EMAIL = 'EMAIL', _('Email')
    PHONE = 'PHONE', _('Phone')
    FACEBOOK = 'FACEBOOK', _('Facebook')
    TELEGRAM = 'TELEGRAM', _('Telegram')
    INSTAGRAM = 'INSTAGRAM', _('Instagram')


class Contact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='contacts')
    picture = models.ImageField(editable=False, blank=True)
    type = models.CharField(max_length=16, choices=ContactType.choices)
    value = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.picture = f'{self.type}.png'.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.value


class ContactHistory(models.Model):
    class Meta:
        verbose_name_plural = 'Contact history'

    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_history')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='contact_history')
    date = models.DateTimeField()

    def __str__(self):
        return self.contact.__str__()