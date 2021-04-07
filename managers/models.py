from django.contrib.auth import get_user_model
from django.db import models
from companies.models import Company

User = get_user_model()


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='managers')

    def __str__(self):
        return self.user
