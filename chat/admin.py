from django.contrib import admin
from chat import models

class PostAdmin(admin.ModelAdmin):
    list_display=('nickname', 'message', 'enabled', 'pub_time')
    ordering=('-pub_time',)
admin.site.register(models.Mood)
admin.site.register(models.Post, PostAdmin)
#资料模型
from .models import Doc
admin.site.register(Doc)
