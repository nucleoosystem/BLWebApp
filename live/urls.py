from django.urls import path

from django.views.generic import View 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Home/', views.Home.as_view(), name='Home'),
    path('about/', views.About.as_view(), name='about'),
    path('sermon/', views.Sermon.as_view(), name='sermon'),
    path('login', views.Login.as_view(), name='login'),

]