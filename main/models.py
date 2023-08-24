from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create predefined categories
Category.objects.get_or_create(name='Technical')
Category.objects.get_or_create(name='Daily')
Category.objects.get_or_create(name='Devotional')
Category.objects.get_or_create(name='Crazy Masti')

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    keywords = models.CharField(max_length=20, null=True)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    nearest_mark = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)
    bio = models.TextField()
    liked_blogs = models.ManyToManyField(Blog, related_name='liked_users')
    is_author = models.BooleanField(default=False)
