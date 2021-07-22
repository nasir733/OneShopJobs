from django.shortcuts import render

# Create your views here.

def LandingPage(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request,'website/dashboard.html')
        return render(request, 'website/landing.html')
    
def dashboardPage(request):
    if request.method == 'GET':
        return render(request,'website/dashboard.html')