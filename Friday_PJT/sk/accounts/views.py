from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from .forms import CustomUserlChangeForm, CustomUserlCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method =='POST':
        form = CustomUserlCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserlCreationForm()
    context = { 
        'form' : form
    }
    return render(request,'accounts/signup.html',context)
        

@require_http_methods(['GET','POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context={
        'form' : form
    }
    return render(request,'accounts/login.html' , context)


def logout(request):
    auth_logout(request)
    return redirect('boards:index')


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('boards:index')

@login_required
@require_http_methods(['POST'])
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    username=person.username
    return redirect('accounts:profile',username)

@require_http_methods(['GET'])
def profile(request,username):
    User = get_user_model()
    person = User.objects.get(username = username)
    context ={
        'person':person
    }
    return render(request,'accounts/profile.html',context)
    