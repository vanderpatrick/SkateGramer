# All necessary imports for the app views

from django.shortcuts import render, redirect
from .models import (Post, Comment, Profile, PostTutorial)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages

# All views used in the app

def landing(request):
    return render(request, 'landing.html')


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-created_on']


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'create'
    fields = ['title', 'image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostTutorialListView(ListView):
    model = PostTutorial
    template_name = 'post_tutorial.html'
    context_object_name = 'tutorial'
    ordering = ['-created_on']
