from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from main.models import *
from django.contrib.auth.models import User

import json
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-written_date')
    games = Game.objects.order_by('game')
    
    try:
        if request.session['error']:
            error_message = request.session['error']
            del request.session['error']
    except KeyError:
        error_message = None
    
    context = {
        'articles': articles,
        'games':games
    }
    return render(request, 'index1.html',context)

def signup(request):

    try:
        if request.session['error']:
            error_message = request.session['error']
            del request.session['error']
    except KeyError:
        error_message = None
    
    context = {
        'error_message' : error_message,
        'title' : 'create ID_31Nov',
        'h4' : '회원가입'
    }
    return render(request, 'signup.html', context)

def signup_submit(request):
    try:
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        password_confirm = request.POST['password_confirm'].strip()
        userPic = request.POST['userPic'].strip()
        
        user = User(username = username, )
        user.set_password(password)
        user.save()
        return redirect('index')
    except KeyError:
        request.session['error'] = '올바른 요청이 아닙니다.'
        return redirect('signup')
    else:
        request.session['error'] = '입력한 정보가 올바르지 않습니다.'
        return redirect('signup')

def user_logout(request):
    logout(request)
    return redirect('index')    
    
def write(request):
    context = {
            
    }
    return render(request, 'write.html',context)


#@login_required
#def write(request):
#    try:
#        if request.session['error']:
#            error_message = request.session['error']
#            del request.session['error']
#    except KeyError:
#        error_message = None
#    
#    context = {
#        'error_message' : error_message
#    }
#    
#    return render(request, 'write.html', context)

