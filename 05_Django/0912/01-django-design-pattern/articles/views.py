from django.shortcuts import render

# Create your views here.
def index(request): # request 안넣으면 작동 안한다!! 
    # 메인 페이지를 응답
    return render(request, 'articles/index.html') # 요청과 함께 템플릿 경로