from django.shortcuts import render
from django.views.generic import DetailView
from .models import FullArticle


class FullArticleDetailView(DetailView):
    model = FullArticle
    template_name = 'article/full-article.html'
    