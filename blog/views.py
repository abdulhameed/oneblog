from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts':posts})


def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(blog_list)
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form':form})


def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(blog_list)
    else:
        form = BlogPostForm()
    return render(request, 'blog/edit_post.html', {'form':form})