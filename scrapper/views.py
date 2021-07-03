from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from .stackoverflowScrapper import extract_jobs, get_last_page, extract_jobs
from .models import Jobs , JobCategory
from icecream import ic
import aiohttp
import asyncio
list_of_jobs = []



async def startScrapper(request):
    print("hello from stackoverflow jobs section")
    jobsName=JobCategory.objects.all()
    for job in jobsName:
        url = f"https://stackoverflow.com/jobs?q=python"
        jobs = extract_jobs(9, url, job)