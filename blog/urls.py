from django.urls import path
from . import views
from article.views import (article_list_view, display_full_article)
from project.views import project_list_view




urlpatterns = [
    path('', views.home, name="blog-home"),
    path('projects/', project_list_view , name='project-full-list'),
    path('listview_content/<str:type>/', article_list_view, name='article-listview'),
    path('full-article/<int:pk>/', display_full_article, name='article-fullview')
]
