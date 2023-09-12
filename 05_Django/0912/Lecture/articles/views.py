from django.shortcuts import render

# Create your views here.
# 특정 경로에 대한 처리를 해줄 함수 

# 매개변수 이름은 내 마음대로 지어도 되는데
# framework 쓸 때는 되도록 Convention 지키자
# request : 사용장의 요청에 대한 모든 정보 
def index(request):
    # 함수가 할 일 정의
    # articles 앱의 메인 페이지를 사용자에게 전달
    # render 함수의 두 번째 인자 template_name은 
    # 정확히는 template이 위치한 경로
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')
