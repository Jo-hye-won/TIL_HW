from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list),
    path('posts/', views.post_list_create),
    path('posts/<int:post_pk>/', views.post_detail),
]
