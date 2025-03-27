from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import  CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username','email','<PASSWORD>',)
