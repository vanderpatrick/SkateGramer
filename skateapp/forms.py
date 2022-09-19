from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post
from ckeditor.fields import RichTextField


class UserRegister(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpadateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateUserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','description']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'content']

