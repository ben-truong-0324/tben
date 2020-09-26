# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from itertools import chain
from time import perf_counter 
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings
from django.urls import reverse_lazy
from django.db.models import Q 
# from .forms import  ContactForm, TeamMemberForm,HIWForm
from django.core.mail import EmailMessage

MAPBOX_TOKEN = settings.MAPBOX_TOKEN
SM_LINKS = settings.SOCIAL_MEDIA_LINKS

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def view_error(request, exception=None):
    # make a redirect to homepage
    return redirect('/') 

def landing(request):
  # if request.method == 'GET':
  #     try:
  #       query = request.GET.get('query')
  #       if query:
  #         redirect_url = reverse_lazy('home:search')
  #         extra_params = '?query_org=%s' % query
  #         full_redirect_url = '%s%s' % (redirect_url, extra_params)
  #         return HttpResponseRedirect( full_redirect_url )
  #     except Exception as e: print(e)

  context = {'sms':SM_LINKS,
              }
  return render(request, 'home/landing.html',context)

def about(request):
  context = {
  }
  return render(request, 'home/about.html',context)

def websites(request):
  context = {
  }
  return render(request, 'home/websites.html',context)

def resume(request):
  context = {
  }
  return render(request, 'home/resume.html',context)

def contact(request):
  context = {
  }
  return render(request, 'home/contact.html',context)
def contactSuccess(request):
  context = {
  }
  return render(request, 'home/contactSuccess.html',context)