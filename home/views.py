''' Imports '''
from django.shortcuts import render
from django.contrib import messages
from .forms import NewsForm
from .models import Subscribe


def index(request):
    """ A view to return the index page with news form included """
    form = NewsForm(request.POST)
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # create a instance variable to check for already subscribed emails
            instance = form.save(commit=False)
            if Subscribe.objects.filter(email=instance.email).exists():
                messages.warning(request, "You are already subscribed!")
                form = NewsForm()
                return render(request, 'home/index.html', {'form': form})
            else:
                instance.save()
                messages.success(request, "Thanks for subscribing!")
                form = NewsForm()
                return render(request, 'home/index.html', {'form': form})
    form = NewsForm()
    return render(request, 'home/index.html', {'form': form})


def unsubscribe(request):
    """ A view to return the unsubscribe page with form included """
    form = NewsForm(request.POST)
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # create a instance variable to check for already subscribed emails
            instance = form.save(commit=False)
            if Subscribe.objects.filter(email=instance.email).exists():
                # delete Subscriber
                messages.success(request, "we're sorry to lose you as a subscriber, \
                    feel free to subscribe again anytime.")
                form = NewsForm()
                return render(request, 'home/unsubscribe.html', {'form': form})
            else:
                messages.error(request, "There are no subscribers currently \
                    using this email.")
                form = NewsForm()
                return render(request, 'home/unsubscribe.html', {'form': form})
    form = NewsForm()
    return render(request, 'home/unsubscribe.html', {'form': form})
