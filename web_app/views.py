from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def adminloginview(request):
    return render(request,'pizza_web_app/login.html')

def authenticateadmin(request):
    username=request.POST['username']
    password =request.POST['password']
    user = authenticate(username=username,password=password)

    if user is not None:
        login(request,user)
        return redirect('homepage')

    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Credentials")
        return redirect('userlogin')

def homepage(request):
    return render(request,'pizza_web_app/home.html')