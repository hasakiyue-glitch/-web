from django.db import models

# Create your models here.
#留言模型设置
class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)#记录心情状态

    def __str__(self):
        return self.status

class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)#外键连接至mood模型
    nickname = models.CharField(max_length=10, default='不愿意透露身份的人')#张贴者昵称
    message = models.TextField(null=False)#留言内容
    del_pass = models.CharField(max_length=10)#删除密码
    pub_time = models.DateTimeField(auto_now=True)#最后修改时间
    enabled = models.BooleanField(default=False)#选中与否决定是否显示在网页
    
    def __str__(self):
        return self.message
#资料下载
#"资料"模型
import django.utils.timezone as timezone
class Doc(models.Model):
    title = models.CharField(max_length=250, verbose_name='资料名称')
    file = models.FileField(upload_to='Service/',
                            blank=True,
                            verbose_name='文件资料')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "资料"
        verbose_name_plural = verbose_name
