from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render

class LoginForm(forms.Form):
    username = forms.CharField(label="Username:", required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label="Password:", required=True, max_length=100, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    def clean(self):
      user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
      self.user = user
      return self.cleaned_data

@view_function
def process_request(request):
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      print("The form is valid")
      user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
      login(request, user)
      if request.user.is_superuser == True:
        return HttpResponse('<script> window.location.href = "/upload"; </script>')
      else:
        return HttpResponseRedirect('/upload')
  else:
    print("The Method is messed up")

  template_vars = {
    'form': form,
    'now': datetime.now(),
  }
  return dmp_render(request, 'login.html', template_vars)