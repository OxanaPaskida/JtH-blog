from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog_Project

def all_blogs(request):
    blog_projects = Blog_Project.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blog_projects': blog_projects})

def detail(request,blog_id):
    blog = get_object_or_404(Blog_Project, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
