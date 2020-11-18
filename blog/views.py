from django.shortcuts import render
from .models import (article, HomePageProfile)
from django.contrib.auth.models import User
from local_var import *
from django.views.generic import (ListView, DetailView)
from .models import HomePageProfile



#user = User.objects.filter(username=USER).first()

def home(request):
    user = HomePageProfile.objects.filter(pk= 1)[0]
    return render(request, 'blog/home.html', {'user': user})


def projects(request):
    return render(request, 'blog/projects.html')

def under_construction(request):
    return render(request, 'blog/under_construction.html')


class ArticleListView (ListView):
    model = article
    template_name = 'blog/security.html'
    context_object_name = 'articles'


class HomePageDetailView(DetailView):
    model= HomePageProfile
    template_name = 'blog/home.html'
    context_object_name = 'User'


