from django.shortcuts import render
from .models import article
from django.contrib.auth.models import User
from local_var import *
from django.views.generic import ListView


user = User.objects.filter(username=USER).first()

def home(request):
    return render(request, 'blog/home.html', {'user': user})


def projects(request):
    return render(request, 'blog/projects.html')

def under_construction(request):
    return render(request, 'blog/under_construction.html')


class ArticleListView (ListView):
    model = article
    template_name = 'blog/security.html'
    context_object_name = 'articles'

