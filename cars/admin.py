from django.contrib import admin
from .models import *
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):    
    def thumbnail(self,object):
        return format_html('<img src="{}" width="50" style="border-radius:10px;" />'.format(object.car_photo.url))
    
    thumbnail.short_description='photo'
    
    list_display=('id','thumbnail','color','model','is_featured')
    list_display_links=('id','thumbnail','model',)
    list_editable=('is_featured',)
    search_fields=('model',)
    list_filter=('model',)
    
# Register your models here.
admin.site.register(Car,CarAdmin)