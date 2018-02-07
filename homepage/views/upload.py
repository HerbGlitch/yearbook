import os
from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from homepage.models import images
from django.shortcuts import render
from django.http import JsonResponse
from homepage import models as cmod
from django import forms

class uploadForm(forms.Form):
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

@view_function
def delete_Image(request):
	temp_id = request.urlparams[0]
	image_to_delete = images.objects.filter(id = temp_id).delete()
	return HttpResponseRedirect('/upload/')

@view_function
def submit(request):
	temp_id = request.urlparams[0]
	image_to_confirm = images.objects.get(id = temp_id)
	image_to_confirm.submitted = True
	image_to_confirm.save()
	return HttpResponseRedirect('/upload/')


@view_function
def process_request(request):
	if request.urlparams[0] == "":
		form = uploadForm(request, initial=model_to_dict(images))
		if request.method == 'POST':
			form = uploadForm(request.POST, request.FILES)
			multipleFiles = request.FILES.getlist('file_field')
			for mFiles in multipleFiles:
				media = cmod.images()
				media.mainImage = mFiles
				media.user_sent = request.user
				media.save()

		imageqry = cmod.images.objects.all()
		adminBool = False;

		template_vars = {
		'adminBool': adminBool,
		'form': form,
		'now': datetime.now(),
		'imageqry': imageqry,
		'request': request,
		}

		return dmp_render(request, 'upload.html', template_vars)
	elif request.urlparams[0] == "admin":
		imageqry = cmod.images.objects.filter(submitted = True)
		adminBool = True;

		template_vars = {
			'adminBool': adminBool,
			'imageqry': imageqry,
			'request': request,
		}

		return dmp_render(request, 'upload.html', template_vars)
