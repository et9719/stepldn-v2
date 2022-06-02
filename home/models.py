''' Imports '''
from django.db import models


class Newsletter(models.Model):
    ''' Fields needed for newsletter form '''
    email = models.EmailField()

    def __str__(self):
        return self.email

class Unsubscribe(models.Model):
    ''' Fields needed for user to unsubscribe to the newsletter '''
    email = models.EmailField()

    def __str__(self):
        return self.email
