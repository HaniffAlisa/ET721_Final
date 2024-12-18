from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def add_blog(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_blog.html', {'form': form})

def edit_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_list')
    else:
        form = BlogPostForm(instance=blog)
    return render(request, 'blog/edit_blog.html', {'form': form, 'blog': blog})

def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def delete_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect('blog:blog_list')
    return render(request, 'blog/delete_blog.html', {'blog': blog})    