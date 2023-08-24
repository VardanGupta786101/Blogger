from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('blogs/create/', views.create_blog, name='create_blog'),
    path('blogs/edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('blogs/view/<int:blog_id>/', views.view_blog, name='view_blog'),
    path('blogs/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/like/<int:blog_id>/', views.like_blog, name='like_blog'),
    path('user/<int:user_id>/blogs/', views.user_blogs, name='user_blogs'),
    path('blogs/search/', views.search_blogs, name='search_blogs'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', views.search_blogs, name='search_blogs'),
    path('', lambda request: redirect('blog_list'), name='root_redirect'),
]
