from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.TextField()
    ref  = models.OneToOneField(User , on_delete=models.CASCADE)