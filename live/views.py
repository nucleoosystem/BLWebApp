from django.http import HttpResponse
from django.shortcuts import render
from .models import Sermon, Speaker
from django.template import loader
def index(request):
    '''View function for home page site'''
    return render(
        request,
        'index.html')

# Create your views here.
