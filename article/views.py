from django.shortcuts import render
# from django.views.generic import DetailView
from .models import FullArticle
from blog.models import SectionHeader
from .models import Article
from django.core.paginator import Paginator


# class FullArticleDetailView(DetailView):
#     model = FullArticle
#     template_name = 'article/article_fullview.html'

def display_full_article(request, pk):
    context = {
        'object': FullArticle.objects.filter(short_article_id = pk)[0]
    }
    return render(request, 'article/article_fullview.html', context)

def article_list_view(request, type):
    sections = {
        '1' : 'Cybersecurity',
        '2' : 'Software'
    }

    all_projects = Article.objects.filter(category=type)
    paginator = Paginator(all_projects, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'header' : SectionHeader.objects.get(name=sections[type]),
        'page_obj' : page_obj      
    }

    return render(request, 'article/article_listview.html', context)