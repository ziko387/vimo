from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .form import CustomUserCreationForm

# Create your views here.


def intro(request):
    return render (request, 'vimo.html')
@login_required(login_url='login_user')
def home(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('login_user')
        else:
            return render(request,'registration.html',{'form':form})

    else:
        form = CustomUserCreationForm()
    return render(request,'registration.html',{'form':form})






def login_user(request):
    if request.method == "POST":
        form=AuthenticationForm(data= request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')

    else:
        form = AuthenticationForm()#intializrer#
    return render(request,'login.html',{'form':form})



def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def add_task(request):
    if request.method == "POST":
        name=request.POST.get('Name')
        phone_number=request.POST.get('Phone_number')
        email=request.POST.get('Email')





