
from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from django.http import HttpResponse
from .. import dmp_render, dmp_render_to_string
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

@view_function
def process_request(request):

  logout(request)

  return HttpResponseRedirect('/index')