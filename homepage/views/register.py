from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from homepage import models as cmod
from homepage.models import User
from django.contrib.auth.hashers import make_password

class LoginForm(forms.Form):
    username = forms.CharField(label="Username:", required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(label="Email:", required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label="Password:", required=True, max_length=100, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    PassCheck = forms.CharField(label="Password Check:", required=True, max_length=100, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

@view_function
def process_request(request):
  form = LoginForm(initial={})
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
        if form.cleaned_data.get('password') == form.cleaned_data.get('PassCheck'):
            d = cmod.User();
            d.username = form.cleaned_data.get('username')
            d.password = make_password(form.cleaned_data.get('password'))
            d.email = form.cleaned_data.get('email')
            d.DateCreated = datetime.now()
            d.save()  #This saves the groups and permissions
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect('/groupchat/')
        else:
            print("is this working")
  else:
    print("The Method is messed up")

  template_vars = {
    'form': form,
    'now': datetime.now(),
  }
  return dmp_render(request, 'register.html', template_vars)
