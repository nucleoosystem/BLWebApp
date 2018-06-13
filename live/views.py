from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Sermon, Speaker

from django.views.generic.base import TemplateView

class HomePage(TemplateView):

    template_name = 'live/home.html'

#def testhome(request):
#    context = {}
 #   template = "navbar.html"
#    return render(request, template, context, 'navbar.html')

def index(request):
     return render(
         request,
         'index.html'

     )


