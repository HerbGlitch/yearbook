from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from django import forms
from homepage import models as cmod
from homepage.models import images
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect

@view_function
def adminify(request):
	if request.user.is_superuser:
		temp_href = request.urlparams[0]
		request.user.adminify = True
		request.user.save()
		return HttpResponseRedirect('/'+temp_href+'/')
	else:
		temp_href = request.urlparams[0]
		return HttpResponseRedirect('/'+temp_href+'/')

@view_function
def un_adminify(request):
	temp_href = request.urlparams[0]
	request.user.adminify = False
	request.user.save()
	return HttpResponseRedirect('/'+temp_href+'/')

@view_function
def process_request(request):
	context = {
		'now': datetime.now(),
		'page_href': 'index',
	}
	return request.dmp_render('index.html', context)
