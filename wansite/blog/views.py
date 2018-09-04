from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blog/home.html", {'posts': posts})

def year_archive(request):
    return HttpResponse("<p>Hello World</p>")
    # return render(request, "blog/year_archive.hmtl", {})

def month_archive(request):
    return render(request, "blog/month_archive.hmtl", {}) 

def article_detail(request):
    return render(request, "blog/article_detail.hmtl", {}) 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {'post': post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.created_time = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk =post.pk)    
    else:
        # post = Post.objects.filter(pk=pk)
        form = PostForm(instance = post)
        return render(request, 'blog/post_edit.html', {'form':form})
    