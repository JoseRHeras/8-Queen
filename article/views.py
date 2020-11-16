from django.shortcuts import render
from django.views.generic import DetailView
from .models import FullArticle



def article_page(request, pk):
    # print(pk)
    return render(request, 'article/example.html')


class FullArticleDetailView(DetailView):
    model = FullArticle
    template_name = 'article/full-article.html'
    