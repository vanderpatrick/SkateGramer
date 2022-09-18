# All necessary imports for the app views

from django.shortcuts import render, redirect
from .models import Post, Comment, Profile, PostTutorial
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import UserRegister, UpdateUserProfile, UserUpadateForm, PostForm


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


# allows user to delete posts
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

# allows creation of user profile
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form = UserRegister()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpadateForm(request.POST, instance=request.user)
        p_form = UpdateUserProfile(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated')
            return redirect('profile')
    else:
        u_form = UserUpadateForm(instance=request.user)
        p_form = UpdateUserProfile(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
