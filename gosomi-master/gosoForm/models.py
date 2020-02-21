from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to="blog/%Y/%m/%d") # 어디에 업로드할지 지정할 수 있음.
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)            # 하나의 사진은 한명의 사용자에게 속해야 하므로. 1:N의 관계
    # thumname_image = models.ImageField()
    title = models.CharField(max_length = 255)
    comment = models.TextField()
    
    pub_date = models.DateTimeField(auto_now_add=True) # 사용자가 입력하지 않고 업로드 하는 순간 자동으로 세팅이 됨. 
    # profile_pic = models.ImageField(upload_to="blog/profile_pic")  ``