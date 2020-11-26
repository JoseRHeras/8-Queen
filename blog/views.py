from django.shortcuts import render
from .models import (article, HomePageProfile)
from django.views.generic import ListView



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



