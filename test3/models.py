from django.db import models

# Create your models here.
from datetime import datetime, timezone
class TV(models.Model):
    TV_CHOICES = (
        ('现代电视剧', '现代电视剧'),
        ('古', '古'),
    )
    title = models.CharField(max_length=50, verbose_name=' 电视剧名称')
    description = models.TextField(verbose_name='剧情介绍')
    TVType = models.CharField(choices=TV_CHOICES,
                                   max_length=50,
                                   verbose_name='电视剧类型')
    publishDate = models.DateTimeField(max_length=20,default=datetime.now(timezone.utc),verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '电视剧'
        verbose_name_plural = '电视剧'
        ordering = ('-publishDate', )

class TVImg(models.Model):
    tv= models.ForeignKey(TV,
                                related_name='TVImgs',
                                verbose_name='电视剧',
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='movie/',
                              blank=True,
                              verbose_name='剧照')

    class Meta:
        verbose_name = '剧照'
        verbose_name_plural = '剧照'
