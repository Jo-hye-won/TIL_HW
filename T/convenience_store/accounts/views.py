from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from .models import User


# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 유효성 검사 통과하면
            auth_login(request, form.get_user())
            # 로그인하고 나서는 메인페이지로 이동
            return redirect('stores:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('stores:index')


def signup(request):
    if request.method == "POST":
        form =CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stores:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def index(request):
    staffs = User.objects.all()
    context = {
        'staffs': staffs
    }
    return render(request, 'accounts/index.html', context)