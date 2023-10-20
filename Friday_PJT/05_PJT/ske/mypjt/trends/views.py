from django.shortcuts import render, redirect
from .models import Keyword, Trend
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create your views here.
def keyword(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        Keyword.objects.create(name=keyword)
        return redirect('trends:keyword')

    keywords = Keyword.objects.all()
    context = {
        'keywords': keywords,
    }
    return render(request, 'keyword.html', context)

def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    keywords = Keyword.objects.all()
    result = []
    for keyword in keywords:      
        url = f"https://www.google.com/search?q={keyword.name}"
        # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)

        # 열린 페이지 소스를 받아옴
        html = driver.page_source 
        soup = BeautifulSoup(html, "html.parser")

        # div 태그 중 id 가 result-stats 인 요소 검색
        result_stats = soup.select_one("div#result-stats")
        string_data = result_stats.text.split()[-2][:-1]
        result = int(string_data.replace(',', ''))

        if Trend.objects.filter(name=keyword.name, search_period="all").exists():
            trend = Trend.objects.get(name=keyword.name, search_period="all")
            trend.result = result
            trend.save()
        else:
          Trend.objects.create(name=keyword.name, result=result, search_period="all")
    
    trends = Trend.objects.filter(search_period="all")
    context = {
        'trends': trends
    }
    return render(request, 'crawling.html', context)


import matplotlib.pyplot as plt
plt.switch_backend('Agg')

import base64
from io import BytesIO

def crawling_histogram(request):
    trends = Trend.objects.filter(search_period="all")
    x = []
    y = []

    for trend in trends:
        x.append(trend.name)
        y.append(trend.result)

    # 그래프 초기화
    plt.clf()

    # 선 그래프 그리기
    # 큰 그림 생성
    plt.figure(figsize=(10, 6))  # 원하는 크기로 수정 (가로 10, 세로 6)
    plt.bar(x, y, label='Trends')

    # 축과 범례 설정
    plt.xticks(rotation=45)  # x 축 레이블 45도 회전
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.title('Technology Trend Analysis')
    plt.legend()
    plt.grid(True)

    # django view 에서 이미지 형식의 데이터를 직접 전송할 수 없음
    # 버퍼로 저장 -> template 으로 전송해야함
    # BytesIO(): 그래프 이미지를 임시로 저장할 버퍼
    buffer = BytesIO()
    # 그래프를 버퍼에 저장. 이미지 형식은 png 로 설정
    plt.savefig(buffer, format='png')
    # 버퍼의 내용을 base64 로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    # data:image/png;base64:
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'crawling_histogram.html', context)

def crawling_advanced(request):
    keywords = Keyword.objects.all()
    result = []
    for keyword in keywords:      
        url = f"https://www.google.com/search?q={keyword.name}&tbs=qdr:y"
        # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)

        # 열린 페이지 소스를 받아옴
        html = driver.page_source 
        soup = BeautifulSoup(html, "html.parser")

        # div 태그 중 id 가 result-stats 인 요소 검색
        result_stats = soup.select_one("div#result-stats")
        string_data = result_stats.text.split()[-2][:-1]
        result = int(string_data.replace(',', ''))
        
        if Trend.objects.filter(name=keyword.name, search_period="year").exists():
            trend = Trend.objects.get(name=keyword.name, search_period="year")
            trend.result = result
            trend.save()
        else:
          Trend.objects.create(name=keyword.name, result=result, search_period="year")

    # 지난 1년을 기준으로 검색한 결과 필터링
    trends = Trend.objects.filter(search_period="year")
    x = []
    y = []

    for trend in trends:
        x.append(trend.name)
        y.append(trend.result)

    # 그래프 초기화
    plt.clf()

    # 선 그래프 그리기
    # 큰 그림 생성
    plt.figure(figsize=(10, 6))  # 원하는 크기로 수정 (가로 10, 세로 6)
    plt.bar(x, y, label='Trends')

    # 축과 범례 설정
    plt.xticks(rotation=45)  # x 축 레이블 45도 회전
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.title('Technology Trend Analysis')
    plt.legend()
    plt.grid(True)

    # django view 에서 이미지 형식의 데이터를 직접 전송할 수 없음
    # 버퍼로 저장 -> template 으로 전송해야함
    # BytesIO(): 그래프 이미지를 임시로 저장할 버퍼
    buffer = BytesIO()
    # 그래프를 버퍼에 저장. 이미지 형식은 png 로 설정
    plt.savefig(buffer, format='png')
    # 버퍼의 내용을 base64 로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    # data:image/png;base64:
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    
    return render(request, 'crawling_advanced.html', context)
