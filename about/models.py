from django.db import models
from django.utils import timezone

class Department(models.Model):
	about = models.TextField()
	dept_history = models.TextField()
	infra = models.TextField()
	labs = models.TextField()
	hostel = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.about