from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime


class Post(models.Model):
    # title = models.CharField(max_length=30)
    # content = models.TextField(max_length=1000)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # created_date = models.DateTimeField(default=timezone.now)

    # class Meta:
    #     ordering = ['title']
    user_id = models.IntegerField()
    # owner = models.CharField(max_length=20, default="???")
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    body = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def increaseViews(self):
        self.views +=1
        self.save()
