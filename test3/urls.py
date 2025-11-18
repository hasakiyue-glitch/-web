from django.urls import path
from .import views

app_name='test3'

urlpatterns = [
   path('test3/<str:TVstyle>/',views.test3,name='test3'),
   path('TVdetail/<int:id>/',views.TVDetail,name='TVdetail')
]