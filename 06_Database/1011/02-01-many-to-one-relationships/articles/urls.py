from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),

    # 댓글 조회를 위한 pk
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', 
         views.comments_delete, 
         name= 'comments_delete'),
]
