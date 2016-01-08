from django.db import models
from django.utils import timezone


class Post(models.Model):
    
    name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    area_of_specialization = models.CharField(max_length=200)
    no_of_publication = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    phd_student_guided = models.CharField(max_length=200)
    mtech_student_guided = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images')

