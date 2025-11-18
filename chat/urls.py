from django.urls import path
from .import views
app_name='chat'
urlpatterns = [
    path('',views.chat,name='chat'),
    path('load/',views.load,name='load'),
    path('delpost/<int:pid>/<str:del_pass>/', views.delpost),
    path('getDoc/<int:id>/', views.getDoc, name='getDoc'),
    
]
