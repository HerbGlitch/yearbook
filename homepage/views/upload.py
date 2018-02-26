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

# reasons_to_report = (
#     ('Inappropriate', 'Inappropriate Image'),
# 	('Vulger', 'Vulger'),
# 	('Racist', 'Racist'),
# )

class uploadForm(forms.Form):
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

# class reportChoiceForm(forms.Form):
# 	choices = forms.ChoiceField(required = True, choices = reasons_to_report)

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
def approved(request):
	temp_id = request.urlparams[0]
	image_to_confirm = images.objects.get(id = temp_id)
	image_to_confirm.approved = True
	image_to_confirm.save()
	return HttpResponseRedirect('/upload/')

@view_function
def unsubmit(request):
	temp_id = request.urlparams[0]
	image_to_confirm = images.objects.get(id = temp_id)
	image_to_confirm.submitted = False
	image_to_confirm.save()
	return HttpResponseRedirect('/upload/')

@view_function
def report(request):
	temp_id = request.urlparams[0]
	image_to_report = images.objects.get(id = temp_id)
	image_to_report.user_sent.reported = True
	image_to_report.user_sent.save()
	return HttpResponseRedirect('/upload/')

@view_function
def process_request(request):
	if request.user.is_anonymous:
		return HttpResponseRedirect('/login/')
	form = uploadForm(request, initial=model_to_dict(images))
	# form_drop_down = reportChoiceForm()
	if request.urlparams[0] == "":
		if request.method == 'POST':
			form = uploadForm(request.POST, request.FILES)
			multipleFiles = request.FILES.getlist('file_field')
			for mFiles in multipleFiles:
				media = cmod.images()
				media.mainImage = mFiles
				media.user_sent = request.user
				media.save()
		if request.user.adminify:
			imageqry = cmod.images.objects.filter(user_sent = request.user)
		else:
			imageqry = images.objects.filter(submitted = True)

	elif request.urlparams[0] == "admin":
		imageqry = images.objects.filter(submitted = True)

	template_vars = {
	'form': form,
	# 'form_drop_down': form_drop_down,
	'now': datetime.now(),
	'imageqry': imageqry,
	'request': request,
	'page_href': 'upload',
	}

	return dmp_render(request, 'upload.html', template_vars)
