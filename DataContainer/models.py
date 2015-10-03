from django.db import models

# Create your models here.
class Container(models.Model):
	id_container    = models.CharField(max_length=255)
	text     = models.TextField()
	created  = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)