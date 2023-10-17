from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 다대다 관계는 복수형 변수명 사용하기
    # 자기자신을 참조(자기자신과 다대다 관계  => self)
    # symmetrical=True (대칭)
    # related_name='followers'역참조 함수 이름 설정
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

