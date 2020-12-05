from django.core.exceptions import AppRegistryNotReady
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import (FullArticle, Article)
from blog.models import SectionHeader
from django.core.paginator import Paginator


def display_full_article(request, pk):
    context = {
        'object': FullArticle.objects.filter(short_article_id = pk)[0]
    }
    return render(request, 'article/article_fullview.html', context)

def article_list_view(request, category_id):
    sections = {'1' : 'Cybersecurity', '2' : 'Software'}
    header = SectionHeader.objects.get(name=sections[category_id])

    if Article.is_there_articles(category_id):
        all_projects = Article.objects.filter(category=category_id)
        paginator = Paginator(all_projects, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {              
            'header' : header,
            'page_obj' : page_obj}

        return render(request, 'article/article_listview.html', context)
    else:
        context = {'header' : header}
        return render(request, 'article/no_articles_available.html', context)
