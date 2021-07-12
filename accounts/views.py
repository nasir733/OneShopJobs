from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def login(request):
    if request.method == "POST":
        username= request.POST['username']
        password=request.POST['password']
        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request=request,user=user)
            messages.success(request, 'you are logged in ')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credintials')
            return redirect('login')
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
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exits')
                else:
                    user =User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,)
                    user.save()
                    messages.success(request, 'Account created succesfully')
                    return redirect('login')

        
        else:
            messages.error(request,'password do not match')
            return redirect('register')
    return render(request,'accounts/registeration.html')