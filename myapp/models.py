from django.db import models


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=30)
    repeat_pass = models.CharField(max_length=30)
