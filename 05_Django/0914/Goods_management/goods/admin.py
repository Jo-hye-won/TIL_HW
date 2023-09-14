from django.contrib import admin
from .models import Article

# Register your models here.
# 관리자.사이트.등록(모델명)
# 아. 싸. 리(모델명)
admin.site.register(Article)
