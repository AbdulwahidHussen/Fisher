from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Info(models.Model):
    site = models.CharField(max_length=20)
    whos = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=1000)
