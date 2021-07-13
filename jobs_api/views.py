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
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    pagination_class = None

    serializer_class = JobsCategorySerializer
    lookup_field = 'name'
    permission_classes = [IsAuthenticated]


class JobsViewSet(viewsets.ModelViewSet):
    queryset =Jobs.objects.order_by('-created_at')
    serializer_class = JobsSerializer
    lookup_field = 'jobCategory'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    search_fields = (
        'rating',
        'location',
        'title',
        'company_name',
        'created_at',
        'job_by'
    )
    ordering_fields = ["rating", "location", 'created_at', 'jobCategory']
