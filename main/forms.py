from django import forms
from .models import Blog
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'keywords', 'categories', 'image']  # Include 'keywords'''



class LoginForm(AuthenticationForm):
    # You can customize the form here if needed
    pass
from django import forms


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
