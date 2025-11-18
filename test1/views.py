from django.shortcuts import render
from .models import pic
# Create your views here.
def test1(request):
    pp=pic.objects.all()
    return render(request,'test1.html',{'pic':pp,})