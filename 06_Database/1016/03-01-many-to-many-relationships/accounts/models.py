from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

'''
class User(AbstractUser):
    like_articles = models.MTMF('articles.Article') 

해도 되지만 기사가 사람을 좋아요하지는 않으니까 잘 생각해보기 

class Article(models.Model):
    user = model.FK('accounts.User')
=> 기본적으로 제공되는 user사용하고 있을 때
'''
