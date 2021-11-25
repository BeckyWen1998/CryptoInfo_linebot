from django.contrib import admin

# Register your models here.
from IT_help.models import *

class User_Info_Admin(admin.ModelAdmin):
    list_display = ('id','uid','name','pic_url','mtext','mdt')
admin.site.register(User_Info,User_Info_Admin)