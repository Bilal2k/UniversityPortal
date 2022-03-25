from multiprocessing import AuthenticationError
from pickle import NONE
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout 

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")

def loginUser(request):
    if request.method=="POST":
        # check for user validation 
        # ruleTheCourt
        username:str = request.POST.get("username")
        password:str = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(f"username: {username}\npassword: {password}")
        if user is not None:
            login(request, user)
            # the user is authenticated now redirect it to profile panel
            return redirect("/")
        else:
            # user's information does not exist in database 
            return render(request, "login.html")
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")