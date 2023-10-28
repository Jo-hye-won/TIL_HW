from django.urls import path, include
from . import views


app_name = 'trends'
urlpatterns = [
    path('', views.index, name='index'),
    path('keyword/', views.keyword, name='keyword'),
    path('keyword/<int:pk>/', views.keyword_detail, name='keyword_detail'),
    path('crawling/', views.crawling, name='crawling'),
    path('crawling/histogram/', views.crawling_histogram, name='crawling_histogram'),
    path('crawling/advanced/', views.crawling_advanced, name='crawling_advanced'),
]

'''
keyword/ 분석을 원하는 키워드 입력 및 추가
keyword/<int:pk> 키워드 삭제
crawling/ 크롤링 수행 및 결과 개수 출력
crawling/histogram/ 크롤링 수행 및 결과 개수 막대 그래프로 출력
crawling/advanced/ 지난 1년을 기준으로 크롤링 수행 및 결과 개수 막대 그래프 출력
'''