from django.shortcuts import render
from django.http import HttpResponse
from .models import article
from django.contrib.auth.models import User
from local_var import *


user = User.objects.filter(username=USER).first()

def home(request):
    return render(request, 'blog/home.html', {'user': user})

def about(request):
    return HttpResponse('<h1>About</h1>')

def security(request):
    return render(request, 'blog/security.html', {'articles': user.article_set.all()})


def projects(request):
    return render(request, 'blog/projects.html')

def under_construction(request):
    return render(request, 'blog/under_construction.html')