from django.shortcuts import  render
from .models import HomePageProfile


def home(request):
    user = HomePageProfile.objects.filter(pk= 1)[0]
    return render(request, 'blog/home.html', {'user': user})


def error_404_view(request, exception):
    context = {}
    return render(request, "blog/404.html", context)

def error_500_view(request):
    return render(request, 'blog/500.html')

def test(request):  
    return render(request, 'blog/500.html')
