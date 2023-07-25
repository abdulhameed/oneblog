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
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default.jpg')

    #1 python3 manage.py makemigrations
    #2 python3 manage.py migrate