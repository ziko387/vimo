from django import forms
from django.contrib.auth.forms import UserCreationForm,authenticate

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
