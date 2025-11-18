
from django.shortcuts import render, redirect
# Create your views here.
# def chat(request):
#     return render(request,'chat.html')
def load(request):
    return render(request,'load.html')
from chat import models
def chat(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET.get('user_id')
        user_pass = request.GET.get('user_pass')
        user_post = request.GET.get('user_post')
        user_mood = request.GET.get('mood')
    except:
        user_id = None
        message = '如果要张贴信息，那么每一个字段都要填...'

    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message='成功保存！请记得你的编辑密码[{}]!，信息须经审查后才会显示。'.format(user_pass)
    return render(request, 'chat.html', locals())

def delpost(request, pid=None, del_pass=None):
    if del_pass and pid:
        try:
            post = models.Post.objects.get(id=pid)
            if post.del_pass == del_pass:
                post.delete()
        except:
            pass
    return redirect('/chat/')
#资料下载模型
from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse
import os
def read_file(file_name, size):  #分批读取文件
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c
            else:
                break
def getDoc(request, id):
    doc = get_object_or_404(Doc, id=id)
    update_to, filename = str(doc.file).split('/')
    filepath = '%s/media/%s/%s' % (os.getcwd(), update_to, filename)
    response = StreamingHttpResponse(read_file(filepath, 512))
    response['Content-Type'] = 'application/msword'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(
        filename)
    return response
from .models import Doc
def load(request):
    docList = Doc.objects.all().order_by('-publishDate')
    return render(
        request, 'load.html', {
                        'docList': docList, 
        })



