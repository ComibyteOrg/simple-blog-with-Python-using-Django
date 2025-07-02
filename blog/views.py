from random import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title') 
        content = request.POST.get('content')
        post_image = request.FILES.get('image')  # Get the uploaded image file
        

        if not title or not content:
            error = "All fields are required" 
            return render(request, 'create.html', {'error': error, 'title': title, 'content': content})
        
        if len(title) < 5:
            error = "Title must be at least 5 characters"
            return render(request, 'create.html', {'error': error, 'title': title, 'content': content})
        
        # Check if title exist 
        if Post.objects.filter(title=title).exists():
            error = "A post with this title already exists"
            return render(request, 'create.html', {'error': error, 'title': title, 'content': content})

        #save the post to the database
        if not post_image:
            post_image = None
        else:
            random_number = int(random() * 1e10)
            filename = f"{random_number}_{post_image.name}"
            post_image.name = filename

        blog = Post(title=title, content=content, post_image=post_image)
        blog.save()
        return redirect('view')

    return render(request, 'create.html')


def viewPost(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'view.html', {'blog': posts})


def deletePost(request, id): 
    blog = Post.objects.get(id=id)
    blog.delete()
    return redirect('view')


def editPost(request, id):
    blog = Post.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_image = request.FILES.get('image')

        if not title or not content:
            error = "All fields are required"
            return render(request, 'edit.html', {'error': error, 'title': title, 'content': content})

        if len(title) < 5:
            error = "Title must be at least 5 characters"
            return render(request, 'edit.html', {'error': error, 'title': title, 'content': content})

        # Check if title exist
        if Post.objects.filter(title=title).exclude(id=id).exists():
            error = "A post with this title already exists"
            return render(request, 'edit.html', {'error': error, 'title': title, 'content': content, 'post_image': blog.post_image})
        
        # Handle the image upload
        if post_image:
            random_number = int(random() * 1e10)
            filename = f"{random_number}_{post_image.name}"
            post_image.name = filename
            blog.post_image = post_image
        else:
            # If no new image is uploaded, keep the existing one
            post_image = blog.post_image

        # Update the post
        blog.title = title
        blog.content = content
        blog.post_image = post_image
        blog.save()
        return redirect('view')

    return render(request, 'edit.html', {'title': blog.title, 'content': blog.content, 'post_image': blog.post_image})