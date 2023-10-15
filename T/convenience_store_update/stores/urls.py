from django.urls import path, include
from .models import Store, Product
from . import views

app_name = 'stores'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:store_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete')
]
