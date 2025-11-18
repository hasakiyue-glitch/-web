from django.db import models

# 图片加描述模型创建如下.
class pic(models.Model):
    description=models.TextField(max_length=500,blank=True,null=True)#描述
    photo=models.ImageField(upload_to='pic/',blank=True)#图片

class Meta:
    verbose_name='图片和描述'
    verbose_name_plural='图片和描述'