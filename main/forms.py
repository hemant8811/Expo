from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import register, News

class signupForm(UserCreationForm):
    class Meta:
         model=User
         fields=['username','email','password1', 'password2']
class register_form(ModelForm):
    class Meta:
        model=register
        fields=['type']
class news_form(ModelForm):
    class Meta:
        model=News
        fields=['title','text']