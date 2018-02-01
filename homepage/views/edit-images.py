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


@view_function
def process_request(request):
	imageqry = cmod.images.objects.filter(submited=True)

	context = {,
	'imageqry': imageqry,
	'request': request,
	}

	return dmp_render('edit-images.html', context)