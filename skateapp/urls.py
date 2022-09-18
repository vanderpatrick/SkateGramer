from django.urls import path
from .views import (PostListView, landing, PostTutorialListView, PostCreateView, PostEditView, PostDetailView, PostDeleteView)
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', PostListView.as_view(), name='home'),
    path('tutorial/', PostTutorialListView.as_view(), name='tutorial'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

