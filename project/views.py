from django.shortcuts import render

def projects(request):
    return render(request, "project/project_page.html")