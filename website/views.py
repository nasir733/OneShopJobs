from django.shortcuts import render

# Create your views here.

def LandingPage(request):
    if request.method == 'GET':
        return render(request, 'website/landing.html')