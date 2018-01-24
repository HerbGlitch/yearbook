from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from django import forms
from homepage import models as cmod
from homepage.models import images
from django.forms.models import model_to_dict

@view_function
def process_request(request):
	context = {
		'now': datetime.now(),
	}
	return request.dmp_render('index.html', context)
