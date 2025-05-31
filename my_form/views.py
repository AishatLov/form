from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile

# User Sign In
def signIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/store/products')
        else:
            messages.error(request, "Invalid Username or password")
            return render(request, "auth/login.html")

    return render(request, "auth/login.html")

# Create Account
def createAccount(request):
    if request.method == "POST":
        data = request.POST
        username = data['username']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'auth/register.html')

        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=username,
            email=data['email']
        )
        new_user.set_password(data['password'])
        new_user.save()

        # Optionally create a Profile
        Profile.objects.create(user=new_user)

        messages.success(request, "Account created successfully")
        return redirect('/auth/login')

    return render(request, 'auth/register.html')

# Log Out User
def logOutUser(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/store/products')
