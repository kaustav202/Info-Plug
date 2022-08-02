from django.db import models
from mentors.models import Mentor
from students.models import Student

# Create your models here.
class Session(models.Model):
    mentor_name = models.TextField()
    student_name = models.TextField()
    timeslot = models.TextField()
    subject = models.TextField()
    mentor_ref = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student_ref = models.ForeignKey(Student, on_delete=models.CASCADE)