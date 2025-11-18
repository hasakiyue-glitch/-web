from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone

class MyNew(models.Model):
    photo=models.ImageField(upload_to='news/',
                            blank=True,
                            null=True,
                            verbose_name='风貌图')
    NEWS_CHOICES=(
        ('建筑图','建筑图'),
        ('鸟览图','鸟览图'),
        ('蓝图','蓝图'),
    )
    title = models.CharField(max_length=50, verbose_name=' 内容标题')
    description = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='news/images/',
                               filePath='news/files/')
    newType = models.CharField(choices=NEWS_CHOICES,
                               max_length=50,
                               verbose_name='图片类型')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "园区风貌"
        verbose_name_plural = verbose_name

        