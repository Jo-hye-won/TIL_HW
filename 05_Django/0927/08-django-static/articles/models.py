from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    
    # blank = True => 이거 안쓰면 게시글 쓸때마다 이미지를 넣어야 함 
    # 이미지 넣는건 선택사항이기 때문에 이케 해둠
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
