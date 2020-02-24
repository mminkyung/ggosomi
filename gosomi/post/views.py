from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def board(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'board.html', {'posts':posts})

def board_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) 
        if form.is_valid():
            title = form.save(commit=False)
            content = form.save(commit=False)
            post.user = request.user     
            form.save()
            return render(request, 'board.html', {'form' : form})
            # return redirect(home)
    else:
        form = PostForm()

    return render(request, 'board_new.html', {'form': form})

def board_detail(request):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'board_detail.html', {'post': post})