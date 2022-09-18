from django.urls import path
from .views import (PostListView, landing, PostTutorialListView, PostCreateView)
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', PostListView.as_view(), name='home'),
    path('tutorial/', PostTutorialListView.as_view(), name='tutorial'),
    path('new/', PostCreateView.as_view(), name='post-create'),
]