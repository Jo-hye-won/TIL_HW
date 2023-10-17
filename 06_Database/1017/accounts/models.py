from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # django가 제공해주는 user data가 가질 column 이외의
    # 추가 column들이 필요하다면 아래에 필드 정의
    # 주민등록번호 = models.CharField(max_length=14)
    pass