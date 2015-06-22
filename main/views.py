from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
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
        'games':games,
        'error_message': error_message
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
#        userPic = request.POST['userPic'].strip()
        
        if username and password and password_confirm :
            if password == password_confirm:
                user = User(username = username)
                user.set_password(password)
                user.save()
                return redirect('login')

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


@login_required
def write(request):
    try:
        if request.session['error']:
            error_message = request.session['error']
            del request.session['error']
    except KeyError:
        error_message = None
    
    context = {
        'error_message' : error_message
    }
    
    return render(request, 'write.html', context)

@login_required
def submit_write(request):
    try:
        title = request.POST['title'].strip()
        content = request.POST['content'].strip()
        if file_image:
            file_image = request.POST['file_image'].strip()
        else:
            file_image = 'X'
        if file_game_apk :
            file_game_apk = request.POST['file_game_apk'].strip()
        else:
            file_game_apk='X'
        if file_game_ios:
            file_game_ios = request.POST['file_game_ios'].strip()
        else:
            file_game_ios='X'
        if file_game_exe:
            file_game_exe = request.POST['file_game_exe'].strip()
        else:
            file_game_exe = 'X'
        if file_game_mac:
            file_game_mac = request.POST['file_game_mac'].strip()
        else:
            file_game_mac = 'X'

    except KeyError:
        request.session['error']='올바른 요청이 아닙니다.'
        return redirect('write')
    else:
        if title and content:
            article = main.article_set.create(title=title, content=content, file_image = file_image, file_game_apk = file_game_apk, file_game_ios = file_game_ios, file_game_exe = file_game_exe, file_game_mac = file_game_mac, user_id=request.user.id)
        else:
            request.session['error'] = '글 제목 혹은 내용을 입력해주세요.'
            return redirect('write')
    return redirect('index')



























