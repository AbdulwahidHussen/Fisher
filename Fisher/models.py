from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserOrder(models.Model):
    site = models.CharField(max_length=20)
    whos = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=20)

class UInfo(models.Model):
    info = models.CharField(max_length=1000)
    user = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
