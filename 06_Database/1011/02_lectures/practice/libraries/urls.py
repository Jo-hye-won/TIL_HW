from django.urls import path
from . import views

app_name = 'libraries'
urlpatterns = [
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_pk>/', views.detail, name='detail'),
    path('<int:author_pk>/books/create/', views.book_create, name='book_create'),
]
