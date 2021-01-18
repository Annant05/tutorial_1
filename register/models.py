from django.db import models


# Create your models here.
class Student(models.Model):
    stds = ((1, '1st'),
            (2, '2nd'),
            (3, '3rd'),
            (4, '4th'),
            (5, '5th'),
            (6, '6th'),
            (7, '7th'),
            (8, '8th'),
            (9, '9th'),
            (10, '10th'),
            (11, '11th'),
            (12, '12th'))
    email = models.CharField(max_length=30)
    rollno = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    std = models.IntegerField(choices=stds)
    city = models.CharField(max_length=10)
