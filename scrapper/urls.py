from django.urls import path, include
from . import views

urlpatterns = [
    path('test-async/', views.startAsyncScrapper),
    path('test-sync/', views.startSyncScrapper)

]
