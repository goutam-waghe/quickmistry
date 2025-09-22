from django.shortcuts import render  , redirect
from users import forms 
from django.contrib.auth import authenticate, login, logout
from users import models

def register(request):
    print("hello")

    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else :
        form = forms.RegisterForm()
    return render(request, "users/register.html",  {'form' : form})


def user_login(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            login(request, user)
            print(request , user.role)
            if user.role == 'customer':
                return redirect("/dashboard/customer")
            else:
                if not user.serviceCategory or not user.skills or not user.experience or not user.rate:
                    return redirect("/dashboard/worker-details")
                else:
                    return redirect("/dashboard/worker")

            
    else:
        form = forms.LoginForm()
    return render(request , 'users/login.html' , {'form': form})


def startPage(request):
    if request.user.is_authenticated:
        if request.user.role == "customer":
            return redirect("dashboard/customer/")  
        elif request.user.role == "worker":
            return redirect("dashboard/worker/")  

    return render(request, "users/startScreen.html")


def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request , 'users/home.html' )




