from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            
            return redirect('accounts:index')        
    else:  
        # 사용자가 직접 입력할 비어있는 form 태그를 만들 것이니..
        # 뭐 특별히 아무것도 안하고 그냥 그대로 만들어서 넘기면 될 듯
        form = AuthenticationForm()

    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)



def index(request):
    # 모든 유저 정보 
    # 아래의 방식은 내일부터는 안쓸거임. 
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'accounts/index.html', context)

def socre_increase(request,user_pk):
    user = User.object.get(pk=user_pk)
    # 파이썬에서 user 변수의 값 score 만 100 증가 시킨 것
    user.score += 100
    # db에 반영
    user.save()
    return redirect('accounts:index')