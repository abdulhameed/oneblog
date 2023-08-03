from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Comments
from .forms import BlogPostForm, CommentForm
# Create your views here.

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required  # This decorator ensures only authenticated users can access the view
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Save the form data but don't commit it to the database yet
            post.author = request.user  # Set the author to the currently logged-in user
            post.save()  # Now save the post with the author information
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})


@login_required  # This decorator ensures only authenticated users can access the view
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            form = BlogPostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect(blog_list)
        else:
            form = BlogPostForm(instance=post)
        return render(request, 'blog/edit_post.html', {'form':form})


@login_required  # This decorator ensures only authenticated users can access the view
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')

    return render(request, 'blog/delete_post.html', {'post': post})


@login_required  # This decorator ensures only authenticated users can access the view
def add_comment_to_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})