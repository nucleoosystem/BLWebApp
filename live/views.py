from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Sermon, Speaker

from django.views.generic.base import TemplateView

class Home(TemplateView):

    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Sermon(TemplateView):
    template_name = 'sermon.html'

class Login(TemplateView):
    template_name = 'login.html'



#def testhome(request):
#    context = {}
 #   template = "navbar.html"
#    return render(request, template, context, 'navbar.html')

def index(request):
     return render(
         request,
         'index.html'

     )


