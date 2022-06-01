''' Imports '''
from django.shortcuts import render
from .forms import ContactForm


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
