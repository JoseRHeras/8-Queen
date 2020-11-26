from django.urls import path
from . import views
from .views import ArticleListView
from article.views import FullArticleDetailView
from project.views import (ProjectListView, project_list_view)



urlpatterns = [
    path('', views.home, name="blog-home"),
    path('security/', ArticleListView.as_view(), name='blog-security'),
    path('underconstruction/', views.under_construction, name='blog-underconstruction'),
    path('full-article/<int:pk>/', FullArticleDetailView.as_view(), name='full-article-view'),
    # path('projects/', ProjectListView.as_view(), name='project-full-list')
    path('projects/', project_list_view , name='project-full-list')
]
