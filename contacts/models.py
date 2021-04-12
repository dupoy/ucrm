from django.db import models
from customers.models import Customer


class Contact(models.Model):
    EMAIL = 'EMAIL'
    PHONE = 'PHONE'
    FACEBOOK = 'FACEBOOK'
    TELEGRAM = 'TELEGRAM'
    INSTAGRAM = 'INSTAGRAM'

    CONTACT_TYPE_CHOICES = [
        (EMAIL, 'Email'),
        (PHONE, 'Phone'),
        (FACEBOOK, 'Facebook'),
        (TELEGRAM, 'Telegram'),
        (INSTAGRAM, 'Instagram'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='contacts')
    picture = models.ImageField(editable=False, blank=True)
    type = models.CharField(max_length=16, choices=CONTACT_TYPE_CHOICES)
    value = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.picture = f'{self.type}.png'.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Contact {self.customer} type {self.type}: {self.value}'
