from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Category, Product, Customer, Order, OrderItem, Review, Cart, CartItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.contrib.auth.models import User


def index(request):
    return render(request,'Frontend\homepage.html')

def sign_in(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST["confirm-password"]

        if password != password2:
             messages.error(request, "Passwords don't match")

        else:
            pass 

        if user_name and email and password and password2:
            hashed_password = make_password(password)
            user = User.objects.create(user_name = user_name, email = email, password = hashed_password)
            print(user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request,"Enter all the fields")

    return render(request,'Frontend/signup.html')


def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if not email or not password:
            messages.error(request, "Please fill in all fields")
            return render(request, "Frontend/login.html")

        user = User.objects.get(email = email)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Wrong credentials")

    return render(request, "Frontend/login.html")


def log_out(request):
    logout(request)

    return render(request,"Frontend/login.html",{
        "message" : "Logged out"
    })


def contact(request):
    return render(request,"Frontend/contact.html")


def shop(request):
    return render(request,"Frontend/shop.html")

def about(request):
    return render(request,"Frontend/about.html")
