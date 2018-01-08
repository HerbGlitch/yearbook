from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from django.forms import ModelMultipleChoiceField
from datetime import date
from django.utils import timezone
from datetime import *
from django.contrib.auth.models import AbstractUser
from django.forms.models import model_to_dict

class User(AbstractUser):
	email = models.EmailField(max_length=200, blank=True)
	userType = models.CharField(max_length=200, null=True, blank=True, default='')
	token = models.IntegerField(default=0)
# Create your models here.
class images(models.Model):
	mainImage = models.ImageField(upload_to='', null=True, blank=True)