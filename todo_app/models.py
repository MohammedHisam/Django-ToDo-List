from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
