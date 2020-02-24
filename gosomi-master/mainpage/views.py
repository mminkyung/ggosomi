from django.shortcuts import render, redirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from gosoForm.models import Photo
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    # user = request.user
    if request.method == "POST":
        username = request.POST['userid']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'home.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'home.html')

def logout(request):
    if request.method == "GET":
        auth.logout(request)
        return redirect('/')
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":     
        if request.POST['password'] == request.POST['password_confirm']:
                err=0
                user = User.objects.create_user(
                    request.POST['username'],
                    password = request.POST['password'],
                    email = request.POST['email'],
                    
                )
                user.profile.job = request.POST['job']
                user.profile.location = request.POST['location']
                user.is_active = False
                user.save()
                auth.login(request,user)
                print( user.profile.job)
                print( user.profile.location)

                current_site = get_current_site(request) 
                    # localhost:8000
                message = render_to_string('user_activate_email.html',{
                        'user': user,
                        'domain': current_site.domain,
                        # 'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                        'token': account_activation_token.make_token(user),
                    })
                print(message)
                # auth.login(request,user)
                mail_subject = "Gosomi 회원가입 인증 메일입니다."
                user_email = user.email
                email = EmailMessage(mail_subject, message, to=[user_email])
                email.send()
                return render(request,'assignment.html')

                # return redirect('account:home')
        # return render(request, 'account/signup.html')
        else:
            err=1
            return render(request, 'signup.html',{'err' : err})

    return render(request, 'signup.html')


def activate(request, uid64, token):

    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('/')
    else:
        return HttpResponse('비정상적인 접근입니다.')

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.job = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()    


def mypage(request):
    user = request.user

    page = request.GET.get('page')
        
    imagePost= Photo.objects.all().order_by('-id')
    photo_paginator = Paginator(imagePost, 3)
    page_photo = photo_paginator.get_page(page)

    if user.is_authenticated == False:
        err_mypage = 0
        return redirect('home')
        #  return HttpResponse('사용자명이 이미 존재합니다.')

    if user.is_staff == False:
        user_job=user.profile.job
        user_loc=user.profile.location
        user_name=user.username
        email=user.email
        return render(request, 'mypage.html', {'imagePost':imagePost, 'page_photo' : page_photo,'name':user_name,'job':user_job, 'location':user_loc, 'email':email})
    else:
        users =  User.objects.all()
        user_job=user.profile.job
        user_loc=user.profile.location
        user_name=user.username
        return render(request, 'staffpage.html', {'imagePost':imagePost, 'page_photo' : page_photo,'name':user_name,'job':user_job, 'location':user_loc, 'user_data':users})


def checkid(request):
    try:
        user = User.objects.get(username=request.GET['username'])
    except Exception as e:
        user = None
    result = {
        'result':'success',
        # 'data' : model_to_dict(user)  # console에서 확인
        'data' : "not exist" if user is None else "exist"
    }
    return JsonResponse(result)