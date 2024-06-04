# blog_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import BlogPost

# Create your views here.
@login_required
def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_app/index.html', {'posts':posts})

@permission_required('blog_app.add_blogpost', login_url='index')
def add_post(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Below is the ORM to create a new post record in the BlogPost table
        BlogPost.objects.create(author=author, title=title, content=content)
        # When done, return to the index.html page
        return redirect('index')
    return render(request, 'blog_app/add_post.html')

@login_required
def view_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_app/view_post.html', {'post': post})

@permission_required('blog_app.change_blogpost', login_url='index')          
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Update the BlogPost record
        post.author = author
        post.title = title
        post.content = content
        post.save()
        # Redirect to the view_post page
        return redirect('view_post', post_id=post.id)
    return render(request, 'blog_app/edit_post.html', {'post': post})
