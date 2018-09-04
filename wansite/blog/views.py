from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
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
    