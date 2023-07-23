from django.contrib import admin
from .models import BlogPost

# Register your models here.
admin.site.register(BlogPost)

# 1- python manage.py makemigrations
# 2- python manage.py migrate
# 3- python manage.py createsuperuser
# 4- python manage.py runserver