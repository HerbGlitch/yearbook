from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from django import forms
from homepage import models as cmod
from homepage.models import images
from django.forms.models import model_to_dict

class uploadForm(forms.Form):
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


@view_function
def process_request(request):
	form = uploadForm(request, initial=model_to_dict(images))
	if request.method == 'POST': #just submitted the form
		form = uploadForm(request.POST, request.FILES)
		multipleFiles = request.FILES.getlist('file_field')
		for mFiles in multipleFiles:
			media = cmod.images()
			media.file = mFiles
			media.Name = mFiles
			media.save()
	context = {
		'form': form,
		'now': datetime.now(),
	}
	return request.dmp_render('index.html', context)