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