from django.db import models
from django.urls import reverse

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Sermon(models.Model):
    '''A listing of teachings'''
    name_of_speaker = models.CharField(max_length=200)
    sermon_date = models.DateTimeField(auto_now_add=True)
    church = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500, help_text='Enter a brief description of the sermon')

    def __str__(self):
        '''Return a string representation of the model.'''
        return self.name_of_speaker
    
    def get_absolute_url(self):
        '''Returns the url to access a detailed record for this sermon'''

class Speaker(models.Model):
    '''Model representing a speaker'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        '''Returns the url to access a particular speaker instance'''
        return reverse('speaker-detal', args=[str(self.id)])

    def __str__(self):
        '''String for representing the Model object'''
        return '{0}, {1}'.format(self.last_name, self.first_name)
