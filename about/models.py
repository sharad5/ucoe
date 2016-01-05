from django.db import models
from django.utils import timezone


class About_home(models.Model):    
    about = models.TextField()
class Dept_history(models.Model):
    dept_history = models.TextField()
class Infrastructure(models.Model):
    infra = models.TextField()
class Labs(models.Model):
    labs = models.TextField()
class Hostel(models.Model):
    hostel = models.TextField()
  