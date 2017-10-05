from django.db import models
from datetime import *
# Create your models here.
class images(models.Model):
	mainImage = models.ImageField(upload_to='', null=True, blank=True)