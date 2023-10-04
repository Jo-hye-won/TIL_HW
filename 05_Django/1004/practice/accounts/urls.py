from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('<int:user_pk>/socre/', views.socre_increase, name= 'socre_increase')
]
