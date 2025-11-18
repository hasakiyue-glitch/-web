from django.urls import path
from .import views

app_name='test2'

urlpatterns = [
    path('',views.tt2,name='test2'),
    path('tt1/',views.t21,name='tt1'),
    path('tt2/<str:newName>/',views.t22,name='tt2'),#新闻列表
    path('newdetail/<int:id>/',views.newdetail,name='newdetail')
]