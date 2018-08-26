from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""
    username = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Email Address'}))    
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
   