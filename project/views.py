from django.shortcuts import render
from django.views.generic import ListView
from .models import Project
from django.core.paginator import Paginator
from blog.models import SectionHeader


class ProjectListView(ListView):
    model = Project


def project_list_view(request):
    all_projects = Project.objects.all()
    paginator = Paginator(all_projects, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'header' : SectionHeader.objects.get(name="Projects"),
        'page_obj' : page_obj      
    }

    return render(request, 'project/project_list.html', context)
