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