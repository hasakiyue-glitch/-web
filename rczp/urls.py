from django.urls import path
from .import views

app_name='rczp'

urlpatterns = [
    path('contact/',views.contact,name='contact'),
    path('recruit/',views.recruit,name='recruit'),
]