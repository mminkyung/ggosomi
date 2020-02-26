from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
# from .forms import PostForm
from django.core.paginator import Paginator

def board(request):
    user = request.user
    # posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.all().order_by('-id')
    post_paginator = Paginator(posts, 8)
    page = request.GET.get('page')
    page_posts = post_paginator.get_page(page)
    # return render(request, 'postpage.html', {'imagePost' : imagePost})

    return render(request, 'board.html', {'page_posts' : page_posts})

def board_create(request):
    user = request.user
    post = Post()
    post.user_id = user.id
    post.onwer = user.username
    post.title = request.POST.get('title')
    post.body = request.POST.get('body')
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('board')

def board_new(request):
    return render(request, 'board_new.html')

def board_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.increaseViews()
    return render(request, 'board_detail.html', {'post': post})

def board_delete(request, post_id):
    post = Post.objects.filter(id=post_id)
    post.delete()
    return redirect('board')

def board_edit(request, post_id):
    post= get_object_or_404(Post, pk= post_id) 
    return render(request, 'editboard.html', {'post': post})

def board_update(request,post_id):
    post= get_object_or_404(Post, pk= post_id) # 특정 객체 가져오기(없으면 404 에러)
    post.title = request.GET['title'] # 내용 채우기
    post.body = request.GET['body'] # 내용 채우기
    post.pub_date = timezone.datetime.now() # 내용 채우기
    post.save() # 저장하기

    # 새로운 글 url 주소로 이동
    return redirect('board')