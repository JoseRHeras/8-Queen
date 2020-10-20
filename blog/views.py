from django.shortcuts import render
from django.http import HttpResponse
from .models import article_presentation


post = [
    {
        'name' : 'Jose Heras'
    }
]

def home(request):
    context = {
        'posts' : post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return HttpResponse('<h1>About</h1>')



def security(request):
    context = {
        'articles' : article_presentation.objects.all()
    }
    return render(request, 'blog/security.html', context)



def projects(request):
    return render(request, 'blog/projects.html')