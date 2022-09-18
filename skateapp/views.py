# All necessary imports for the app views

from django.shortcuts import render, redirect
from .models import (Post, Comment, Profile, PostTutorial)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages

# All views used in the app

# View to render landing page for new users
def landing(request):
    return render(request, 'landing.html')


# displays list of all posts in the app 
class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-created_on']


# Creates a new post in the app if user is True
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'create'
    fields = ['title', 'image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Displays post details 
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'detail'
    template_name = 'post_detail.html'


# Allow user to update his post if user = True
class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    context_object_name = "update"
    fields = ['title', 'image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

# Displays tutorials post made by admin (only)
class PostTutorialListView(ListView):
    model = PostTutorial
    template_name = 'post_tutorial.html'
    context_object_name = 'tutorial'
    ordering = ['-created_on']

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/home'
    template_name = 'post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
