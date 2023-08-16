from django.shortcuts import render, redirect
from .forms import signupForm, register_form, news_form
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from .models import register, News as N
from django.contrib.auth.decorators import login_required, permission_required





# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def sign_up(request):
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('/home')
    else:
        form=signupForm()
    return render(request,'registration/sign_up.html',{"form": form})
@login_required(login_url="login")




def Register(request):
    exists=hasattr(request.user,'register')
    if exists:
        f=True
        return render(request,'main/register.html',{'f':f})
    elif request.method=='POST':
        form=register_form(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.name=request.user
            post.save()
            return redirect('/home')
    else:
        form=register_form()
    return render(request,'main/register.html',{'form':form})
def Userinfo(request):
    User = get_user_model()
    users = User.objects.all()
    user_count=User.objects.all().count()
    register_count=register.objects.all().count()
    return render(request,'main/userinfo.html',{'User':users, 'user_count':user_count,'register_count':register_count})


def News(request):
    news=N.objects.all()
    form=news_form(request.POST)
    if form.is_valid():
        post=form.save(commit=False)
        post.save()
        return redirect('/news')

    return render(request,'main/news.html',{'form':form,'news':news})
