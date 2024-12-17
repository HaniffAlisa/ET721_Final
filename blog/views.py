from django.shortcuts import render, redirect
from .models import BlogPost

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def add_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author', 'Anonymous')
        BlogPost.objects.create(title=title, content=content, author=author)
        return redirect('blog:blog_list')
    return render(request, 'blog/add_blog.html')