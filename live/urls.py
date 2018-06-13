from django.urls import path

from django.views.generic import View 

from . import views

from .views import HomePage

urlpatterns = [
    path('', views.index, name='index'),
#    path('', Views.testhome, name='testhome'),
]