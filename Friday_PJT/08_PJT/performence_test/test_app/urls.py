from django.urls import path
from . import views

urlpatterns = [
    path('normal_sort/', views.normal_sort),
    path('priority_queue/', views.priority_queue),
    path('bubble_sort/', views.bubble_sort),
    path('read_csv_data/', views.read_csv_data),
    path('B/', views.B),
    path('C/', views.C),
    path('db_analysis/', views.db_analysis)
]

