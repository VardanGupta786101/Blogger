from django.contrib import admin
from .models import Blog, Category, UserProfile

# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(UserProfile)
