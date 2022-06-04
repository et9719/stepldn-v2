''' Imports'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('view_contact/', views.read_contact_view, name='view_contact'),
]
