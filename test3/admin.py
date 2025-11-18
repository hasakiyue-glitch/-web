from django.contrib import admin

# Register your models here.
from .models import TV,TVImg
# admin.site.register(TV)
# admin.site.register(TVImg)
class TVImgInline(admin.StackedInline):
    model=TVImg
    extra=1

class TVadmin(admin.ModelAdmin):
    inlines=[TVImgInline,]

admin.site.register(TV,TVadmin)
