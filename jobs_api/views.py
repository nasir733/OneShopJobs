from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import JobsSerializer, JobsCategorySerializer
from .models import Jobcategory, Jobs
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.


class Jobscategory(viewsets.ModelViewSet):
    queryset = Jobcategory.objects.all()
    authentication_classes = []

    pagination_class = None

    serializer_class = JobsCategorySerializer
    lookup_field = 'name'
    permission_classes = []


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    lookup_field = 'jobCategory'
    authentication_classes = []
    permission_classes = []
    search_fields = (
        'rating',
        'location',
        'title',
        'company_name',
        'created_at',
        'job_by'
    )
    ordering_fields = ["rating", "location", 'created_at', 'jobCategory']
