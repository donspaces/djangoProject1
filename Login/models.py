from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models

class Pending(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    passwd = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
