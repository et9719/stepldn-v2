''' Imports '''
from django.forms import ModelForm
from .models import Newsletter, Unsubscribe


class NewsForm(ModelForm):
    ''' create a form for users to sign up to the news letter '''
    class Meta:
        ''' Get fields from newsletter model '''
        model = Newsletter
        fields = '__all__'

class UnsubscribeForm(ModelForm):
    ''' create a form for users to sign up to the news letter '''
    class Meta:
        ''' Get fields from newsletter model '''
        model = Newsletter
        fields = '__all__'
