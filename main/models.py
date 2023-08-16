from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



#Create your models
class register(models.Model):
    name=models.OneToOneField(User, on_delete=models.CASCADE)
    type=models.BooleanField(default=False)
    def __str__(self):
        return self.name.username
class News(models.Model):
    title=models.CharField(max_length=20)
    text=models.TextField(max_length=200)
    post_date=models.DateTimeField(auto_now_add=True)
