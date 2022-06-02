''' Imports '''
from django.db import models


class Subscribe(models.Model):
    ''' Fields needed for newsletter form '''
    class Meta:
        ''' Change subscribs to subscribers in admin '''
        verbose_name_plural = 'Subscribers'

    email = models.EmailField()

    def __str__(self):
        return self.email
