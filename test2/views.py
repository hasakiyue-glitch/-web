from django.shortcuts import render
#从富文本中提取文字
from pyquery import PyQuery as pq
# Create your views here.
def tt2(request):
    return render(request,'test2.html')
def t21(request):
    return render(request,'test21.html')
from .models import MyNew
from django.core.paginator import Paginator
def t22(request, newName):
    # 解析请求的新闻类型
    submenu = newName
    if newName == 'movie':
        newName = '招商'
    elif newName == 'people':
        newName = '投资'
    elif newName == 'show':
        newName = '成功'    
    else:
        newName = '空间'
    # 从数据库获取、过滤和排序数据
    newList = MyNew.objects.all().filter(
        newType=newName).order_by('-publishDate')
    #pyquery
    for mynew in newList:
          html = pq(mynew.description)  # 使用pq方法解析html内容
          mynew.mytxt = pq(html)('p').text()  # 截取html段落文字
    #pyquery

    
    # 分页
    p = Paginator(newList, 5)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        newList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageData = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }
    return render(
        request, 'test22.html', {
            'sub_menu': submenu,
            'newName': newName,
            'newList': newList,
            'pageData': pageData,
        })

#news details
from django.shortcuts import get_object_or_404
def newdetail(request,id):
    mynew=get_object_or_404(MyNew,id=id)
    mynew.views+=1
    mynew.save()
    return render(request,'newsdetail.html',{'mynew':mynew,})
