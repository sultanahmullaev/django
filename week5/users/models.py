from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser, models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30, unique=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']
