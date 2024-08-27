from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Office


def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
       username=request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password=password)
       if user is not None:
          auth.login(request,user)
          return render(request,"home.html")
       else:
           messages.info(request,"invalid credentials")
           return redirect('login')
    return render(request,"dashboard.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            # Create a new user
            User.objects.create_user(username=username, password=password)
            # Automatically log the user in after registration
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or another page
    return render(request, 'register.html')

def dashboard(request):
    return render(request,'dashboard.html')


def available_offices(request):
    offices = Office.objects.all()
    return render(request, 'available_offices.html', {'offices': offices})


def office_details(request):
    return render(request,'office_details.html')