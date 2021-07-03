from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from .stackoverflowScrapper import extract_jobs, get_last_page, extract_jobs
from .syncStackOverflowScrapper import extract_jobs as findjob
from .models import Jobs, JobCategory
from icecream import ic
import aiohttp
import asyncio
from channels.db import database_sync_to_async
import time


list_of_jobs = []


# sync Scrapper test
def startSyncScrapper(request):
    print("hello from stackoverflow jobs section")

    start_time = time.time()
    jobsName = JobCategory.objects.all()
    # print(jobsName)
    for job in jobsName:
        url = f"https://stackoverflow.com/jobs?q={job}"
        jobs = findjob(9, url, job)
    total_time = time.time() - start_time

    return HttpResponse(f"hi the syn scrapper is done in {total_time}sec ")

# async scrapper test


@database_sync_to_async
def getJobCategory():
    return list(JobCategory.objects.all())


async def startAsyncScrapper(request):
    print("hello from stackoverflow jobs section")
    actions = []
    start_time = time.time()
    jobsName = await getJobCategory()
    # print(jobsName)
    for job in jobsName:
        url = f"https://stackoverflow.com/jobs?q={job}"
        actions.append(asyncio.ensure_future(extract_jobs(9, url, job)))
    await asyncio.gather(*actions)
    total_time = time.time() - start_time

    return HttpResponse(f"hi the  scrapper is done in {total_time}sec ")
