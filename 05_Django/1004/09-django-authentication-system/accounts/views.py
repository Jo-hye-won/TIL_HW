from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
def login(request):
    if request.method == 'POST':
        # pass # 세션 create하는 부분
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): # 유효성 검사
            # 로그인(세션 데이터 생성)
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else: 
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request): 
    auth_logout(request)
    return redirect('articles:index')

