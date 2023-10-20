from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# 로그인할 때 활용하는 폼
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationFrom

# Create your views here.
@ require_http_methods(['GET', 'POST'])
def signup(request):
    # 로그인한 사용자가 들어오면?
    if request.user.is_authenticated:
        return redirect("boards:index")
    
    # METHOP가 GET일 때와 POST일 때
    # POST : 실제로 회원가입 진행
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            # 저장 및 자동로그인
            user = form.save() # 회원가입하면 user가 반환됨
            auth_login(request, user)
            return redirect("boards:index")

    # GET : 회원가입 페이지 보여줘야 함
    else:
        form = CustomUserCreationFrom()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


@ require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect("boards:index")
    
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
        
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


# 세션 데이터 삭제(DB를 건드린다) => POST 요청
@require_POST
def logout(request):
    # 로그인 안된 사용자가 요청을 보내면?
    # 로그인 된 사용자만 로그아웃 ( 3 :12: 00)
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("boards:index")