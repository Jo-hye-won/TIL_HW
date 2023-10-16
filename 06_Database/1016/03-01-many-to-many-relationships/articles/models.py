from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    # 단수형태
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    # 복수형
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles') # 중개테이블생성됨
    # article.like_users.all() => 이 글에 좋아요를 누를 모든 유저
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
