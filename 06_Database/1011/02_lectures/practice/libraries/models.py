from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birth = models.DateField()
    nationality = models.TextField()

class Book(models.Model):
    # Foreign Key 필드가 있다.
    # 참조 대상의 PK 값을 저장할 필드
    # Author와 Book의 데이터가 1:N의 관계를 맺고 있음.
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    description = models.TextField()
    adult = models.BooleanField()
    price = models.IntegerField()
