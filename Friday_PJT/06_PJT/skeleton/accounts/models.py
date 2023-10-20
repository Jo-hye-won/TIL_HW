from django.db import models
# 어떻게 클래스처럼 . 으로 접근할 수 있을까?
# django github
from django.contrib.auth.models import AbstractUser

# 기본회원 모델 auth.user를 accounts.user로 변경할래 
# Create your models here.
class User(AbstractUser):
    pass
