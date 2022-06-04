''' Imports '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]
