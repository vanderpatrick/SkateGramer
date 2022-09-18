from django.urls import path
from .views import (PostListView, landing)
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', PostListView.as_view(), name='home'),
]