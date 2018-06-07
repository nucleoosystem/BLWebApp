from django.db import models

# Create your models here.

class Teachings(models.Model):
    '''A listing of teachings'''
    text = models.CharField(max_length=200)
    dates_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return a string representation of the model.'''
        return self.text
