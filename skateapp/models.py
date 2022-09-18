# All necessary imports

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.utils.timezone import timezone


# All app models.

# post model responsible for regular post made by (user/admin)
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('home')
    def save(self, *args, **kwargs):
        super().save()

    def __str__(self):
        return self.title

# Comment model responsible for regular comments in Post model by (user/admin)
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.user.username} Comment'

# Profile model responsible for the creation and maintance of the user profile by (user/admin)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    description = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self, *args, **kwargs):
        super().save()

# PostTutorial model responsible for the tutorial post made only by (admin)
class PostTutorial(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title