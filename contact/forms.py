''' Imports '''
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    ''' create contact form '''
    class Meta:
        ''' Get fields from contact model '''
        model = Contact
        fields = '__all__'
