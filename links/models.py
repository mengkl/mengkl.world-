from django.db import models


# Create your models here.

class Friend(models.Model):
    friend_name = models.CharField(max_length=50)
    brief_introduction = models.CharField(max_length=100)
    blog_url = models.URLField()
    blog_avatar_url = models.URLField()

# todo:  名字  charfield   介绍  charfield   博客链接  URLField  头像链接  URLField
