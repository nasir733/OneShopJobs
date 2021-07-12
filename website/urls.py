from .views import *
from django.urls import path, include
urlpatterns = [
    path("", LandingPage, name="landingPage"),
    path('dashboard/',dashboardPage,name='dashboard')
]