''' Imports '''
from django.shortcuts import render
from .forms import NewsForm, UnsubscribeForm


def index(request):
    """ A view to return the index page with news form included """

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html')
    form = NewsForm(request.POST)
    context = {'form': form}
    return render(request, 'home/index.html', context)

def unsubscribe(request):
    """ A view to return the index page with news form included """
    # get list of emails that have subscribed
    # take the email
    # check if it is in the list
    # if it is, remove it
    # if not, say your not subscribed
    if request.method == 'POST':
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/unsubscribe.html')
    form = UnsubscribeForm(request.POST)
    context = {'form': form}
    return render(request, 'home/unsubscribe.html', context)
