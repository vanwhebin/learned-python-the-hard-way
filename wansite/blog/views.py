from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "blog/home.html", {})

def year_archive(request):
    return HttpResponse("<p>Hello World</p>")
    # return render(request, "blog/year_archive.hmtl", {})

def month_archive(request):
    return render(request, "blog/month_archive.hmtl", {}) 

def article_detail(request):
    return render(request, "blog/article_detail.hmtl", {}) 
    