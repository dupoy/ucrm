from django.db import models

from companies.models import Company


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=31, unique=True)
    email = models.EmailField(unique=True)
    note = models.TextField(max_length=500, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_name()
