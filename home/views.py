from django.shortcuts import render
from test3.models import TV
# Create your views here.
def home(request):
    return render(request,'home.html')
from test2.models import MyNew
from django.db.models import Q
def home(request):
    # 新闻展报
    noteList = MyNew.objects.all().filter(Q(newType='杂文趣事')).order_by('-publishDate')
    if (len(noteList) > 4):
        noteList = noteList[0:4]
    TVList=TV.objects.all().order_by('-views')
    if(len(TVList)>4):
        TVList=TVList[0:4]
    newList = MyNew.objects.all().filter(~Q(
        newType='杂文趣事')).order_by('-publishDate')
    postList = set()
    postNum = 0
    for s in newList:
        if s.photo:
            postList.add(s)
            postNum += 1
        if postNum == 3:  # 只截取最近的3个展报
            break

    # 新闻列表
    if (len(newList) > 7):
        newList = newList[0:7]
          # 返回结果
    return render(request, 'home.html', {
    'postList': postList,
        'newList': newList,
        'TVList':TVList,
    })
