from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True
        )
    bio = models.TextField(blank=True)

    # python3 manage.py makemigrations
    # python3 manage.py migrate