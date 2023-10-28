from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm, TrendForm
from bs4 import BeautifulSoup
from selenium import webdriver


# Create your views here.
def index(request):
    return render(request, 'trends/index.html')


# 키워드 저장 및 keyword.html 렌더링
def keyword(request):
    keyword = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)    
        if form.is_valid():
            form.save()
        return redirect('trends:keyword')
    else:        
        form = KeywordForm()
        # keyword = Keyword.objects.all()

    context = {
        'form': form,
        'keyword':keyword
    }
    return render(request, 'trends/keyword.html', context)

# 키워드 삭제 및 keyword.html 로 리다이렉션
def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')


def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    result_stats = soup.select_one("div#result-stats") 
    return result_stats.text


def crawling(request):
    keyword = Keyword.objects.all()
    datas = []
    for key in keyword:
        data = get_google_data(key.name)
        data = data.replace(',', '')
        num = ''
        booli = False
        for i in data:         
            if i.isdigit():
                booli =True
                num += i
            if booli and (not i.isdigit()):
                break
    
        if Trend.objects.filter(name=key.name, search_period='all').exists():
            t = Trend.objects.get(name=key.name,result = int(num), search_period='all')
            t.result = int(num)
            t.save()
        else:
            Trend.objects.create(name=key.name,result = int(num), search_period='all')
    # trends = Trend.objects.all()
    trends = Trend.objects.filter(search_period="all")
    context ={
        'datas': datas,
        'keyword': keyword,
        'trends': trends,
    }
    return render(request, 'trends/crawling.html', context)


# 크롤링 수행 후 수행 결과 막대 그래프 생성 및 crawling_histogram.html 렌더링
def crawling_histogram(request):

    return render(request, 'trends/crawling_histogram.html')



# 지난 1년을 기준으로 크롤링 수행 후 수행 결과 막대 그래프 생성 
# 및 crawling_advanced.html 렌더링
def crawling_advanced(request):
    return render(request, 'trends/crawling_advanced.html')