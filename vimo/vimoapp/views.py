from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.


def intro(request):
    return render (request, 'vimo.html')
@login_required(login_url='login_user')
def home(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        user = authenticate(request, username=username, password=password,phone_number=phone_number)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserCreationForm()
        return render(request,'registration.html',{'form':form})




def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, username=username, password=password,email=email,)
        form = AuthenticationForm(data=request.POST)
        if user and form.is_valid():
            login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()#intializrer#
        messages.error(request, 'Invalid username or password')
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





