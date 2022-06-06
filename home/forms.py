''' Imports '''
from django.forms import ModelForm
from .models import Subscribe


class NewsForm(ModelForm):
    ''' create a form for users to sign up to the news letter '''
    class Meta:
        ''' Get fields from newsletter model '''
        model = Subscribe
        fields = '__all__'
