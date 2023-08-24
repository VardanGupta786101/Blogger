from django import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import BlogForm, LoginForm, RegistrationForm
from .models import Blog, Category, UserProfile


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            if request.user.is_authenticated:
                blog.author = request.user
            else: raise UserWarning 
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})


@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('view_blog', blog_id=blog_id)  # Redirect to the blog detail view
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit.html', {'form': form, 'blog': blog})

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.user.is_authenticated:
        is_author = blog.author == request.user
        return render(request, 'blog/view.html', {'blog': blog, 'is_author': is_author})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.user == blog.author:
        if request.method == 'POST':
            blog.delete()
            return redirect('blog_list')
        return render(request, 'blog/delete_confirm.html', {'blog': blog})
    else:
        return redirect('view_blog', blog_id=blog_id)

@login_required   
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/list.html', {'blogs': blogs})

@login_required
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.liked_blogs.add(blog)
    return redirect('view_blog', blog_id=blog_id)

@login_required
def user_blogs(request, user_id):
    user_profile = UserProfile.objects.filter(user__id__icontains=user_id)
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'blog/user_blogs.html', {'user_profile': user_profile, 'blogs': blogs})

@login_required
def search_blogs(request):
    query = request.GET.get('q')
    blogs = Blog.objects.filter(title__icontains=query) if query else []
    return render(request, 'blog/search_results.html', {'blogs': blogs, 'query': query})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog_list')  # Redirect to a specific page after login
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('blog_list')  # Redirect to a specific page after registration
        else:
             return HttpResponse("Somthing went wrong")
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

def search_blogs(request):
    query = request.GET.get('q')
    blogs = Blog.objects.filter(keywords__icontains=query)
    return render(request, 'blog/search_results.html', {'blogs': blogs, 'query': query})







