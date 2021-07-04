from celery import shared_task
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from .stackoverflowScrapper import extract_jobs, get_last_page, extract_jobs
from .models import Jobs, JobCategory
from icecream import ic
import aiohttp
import asyncio
from channels.db import database_sync_to_async
import time


@database_sync_to_async
def getJobCategory():
    return list(JobCategory.objects.all())


@shared_task()
async def stackoverflowScrapper(request):
    print("hello from stackoverflow jobs section")
    actions = []
    jobsName = await getJobCategory()
    # print(jobsName)
    for job in jobsName:
        url = f"https://stackoverflow.com/jobs?q={job}"
        actions.append(asyncio.ensure_future(extract_jobs(9, url, job)))
    await asyncio.gather(*actions)
