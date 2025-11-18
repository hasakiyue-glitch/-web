
from django.shortcuts import render
from .models import TV
# Create your views here.
# 分页显示
from django.core.paginator import Paginator
# 分页显示
def test3(request,TVstyle):
    if TVstyle=='pass':
        TVstyle='产业现状'
    else:
        TVstyle='头部企业'
   
    TVlist=TV.objects.all().filter(TVType=TVstyle).order_by('-publishDate')
# 分页显示
    p = Paginator(TVlist, 2)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        TVlist = p.page(page)
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

# 分页显示
    return render(request,'test3.html',{
        'TVstyle':TVstyle,
        'TVlist':TVlist,
        'pageData':pageData,
        })

#电视剧详情页面
from  django.shortcuts import get_object_or_404
def TVDetail(request,id):
    tv = get_object_or_404(TV,id=id)
    tv.views += 1
    tv.save()

    return render(request, 'TVdetail.html',{
                'tv':tv,
})
