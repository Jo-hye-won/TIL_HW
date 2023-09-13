from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('',views.find, name = 'index'),
    path('<str:author>/', views.author, name='author_book')
]
