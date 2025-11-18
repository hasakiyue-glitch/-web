from django.urls import path
from .import views

app_name='test1'

urlpatterns = [
    path('',views.test1,name='test1'),
]