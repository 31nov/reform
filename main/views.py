from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from main.models import *
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.datastructures import MultiValueDictKeyError


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
        useremail = request.POST['email'].strip()
        password = request.POST['password'].strip()
        password_confirm = request.POST['password_confirm'].strip()
        
        try:
            pic = request.FILES['userPic']
            nick = pic._name
        except MultiValueDictKeyError:
            pic = ''
            nick = 'none'

        if username and password and password_confirm :
            if password == password_confirm:
                if pic:
                    user = User(username = username, email = useremail)
                    user.set_password(password)
                    user.save()
                    
                    r = Profile(user=user, pic=pic)
                    r.save()
#                    picture = Profile(pic = pic)
#                    picture.save()
#                    userpic = UserAdmin(pic = picture, user_id = user.id)
#                    userpic.save()
                    
                else:
                    user = User(username = username, email = useremail,)
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
    title = request.POST['title'].strip()
    content = request.POST['content'].strip()
    
    try:
        try:
            file_image = request.FILES['file_image']
            imgName = file_image._name
        except MultiValueDictKeyError:
            file_image = ''
            imgName = 'none'
            
        if title and content and imgName:
#            request.session['error']='3가지 충족'
            article = Article(title=title, content=content, file_image = file_image, imgName = imgName, user_id=request.user.id)
            article.save()
            
            return redirect('index')
        elif title and content:
#            request.session['error']='제목&내용 2가지 충족'
            article = Article(title=title, content=content, user_id=request.user.id)
            article.save()
            
            return redirect('index')
        elif title and imgName:
#            request.session['error']='제목&이미지 2가지 충족'
            article = Article(title=title, file_image = file_image, imgName = imgName, user_id=request.user.id)
            article.save()
            
            return redirect('index')
#            request.session['error']='제목만 충족'
        elif title:
            article = Article(title=title, user_id=request.user.id)
            article.save()
        
        else:
            request.session['error']='제목은 입력해야 합니다.'
            return redirect('write')

    except:
        request.session['error']='올바른 요청이 아닙니다.'
        return redirect('write')


























