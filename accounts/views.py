from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def login(request):
    return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect("landingPage")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user =User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,)
        user.save()
        messages.success(request, 'Account created succesfully')
        return redirect('login')
    return render(request,'accounts/registeration.html')