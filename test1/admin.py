from django.contrib import admin
from .models import pic

# Register your models here.
class picAdmin(admin.ModelAdmin):
    list_display=['description','photo']
admin.site.register(pic,picAdmin)
admin.site.site_header="雪梅煮茶"
admin.site.site_title="雪梅煮茶"