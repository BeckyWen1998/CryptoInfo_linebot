from django.db import models


# Create your models here.
class User_Info(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         #user_id
    name = models.CharField(max_length=255,blank=True,null=False)       #LINE名字
    pic_url = models.CharField(max_length=255,null=False)               #大頭貼網址
    mtext = models.CharField(max_length=255,blank=True,null=False)      #文字訊息紀錄
    mdt = models.DateTimeField(auto_now=True)                           #物件儲存的日期時間
    #Table_name.objects.create(data=data)
    #以filter讀取資料庫則將回傳list格式資料列表
    #Table_name.objects.filter(data=data)

    #以get讀取資料庫會獲得單筆資料物件
    #Table_name.objects.get(data=data)
    #Table_name.objects.filter(data=data).update(data=new_data)
    #Table_name.objects.filter(data=data).delete()
    #Table_name.objects.all().delete()

    def __str__(self):
        return self.uid