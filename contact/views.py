''' Imports '''
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Contact


def contact_view(request):
    ''' get forms context and show it on contact.html and direct where is should post to '''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)


@login_required
def read_contact_view(request):
    """ Allow site admin to read messages left through contact form """
    # What model we are using for this view
    model = Contact
    # get messages
    
    # What page admin will be able to see this on
    
