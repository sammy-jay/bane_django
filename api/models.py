from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True, blank=False)
    avatar = models.ImageField(upload_to="uploads/avatars", blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

