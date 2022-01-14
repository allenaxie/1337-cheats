from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Cheatsheet(models.Model):
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)