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
	approved = models.BooleanField(default = False)
	adminify = models.BooleanField(default = False)

class images(models.Model):
	mainImage = models.ImageField(upload_to='homepage/media/', null=True, blank=True)
	submitted = models.BooleanField(default = False)
	approved = models.BooleanField(default = False)
	user_sent = models.ForeignKey(User, null=True, blank=True)

class club(models.Model):
	club_image = models.ImageField(upload_to='homepage/media/', null=True, blank=True)
	title = models.CharField(max_length=200, null=True, blank=True, default='club')
	description = models.TextField()
	members = models.ManyToManyField(User)

class staffers(models.Model):
	staffer = models.ForeignKey(User, null=True, blank=True)
