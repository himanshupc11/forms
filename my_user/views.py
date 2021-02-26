from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_user(request):
    if request.method == "GET":
        return render(request, "my_user/login_user.html")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Successfully logged in")
        else:
            return HttpResponse("Cannot be logged in")

def logout_user(request):
    logout(request)
    return render(request, "my_user/logout_user.html")

def register_user(request):
    if request.method == "GET":
        return render(request, "my_user/register_user.html")
    else:
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            user = User.objects.create_user(username, email, password)
            user.save()
            return HttpResponse("Success")
        except Exception:
            return HttpResponse("Failure as username is not unique")  

def index(request):
    return render(request, "my_user/index.html")