from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mentor(models.Model):
    timeslots = models.TextField()
    subjects = models.TextField()
    ref = models.OneToOneField(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.ref.username
