from django.shortcuts import render
from .models import HomePageProfile


def home(request):
    user = HomePageProfile.objects.filter(pk= 1)[0]
    return render(request, 'blog/home.html', {'user': user})


def under_construction(request):
    return render(request, 'blog/under_construction.html')


def software_project_articles(request):
    return render(request, '')







