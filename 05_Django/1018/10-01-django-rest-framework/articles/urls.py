from django.urls import path
from articles import views

# 이름은 템플릿에서 쓰는데 템플릿 없어서 안해도 됨
urlpatterns = [
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/', views.article_list),
]
