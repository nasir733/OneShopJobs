
from celery import shared_task

# from celery.decorators import periodic_task
# from celery.task.schedules import crontab
from .models import Jobs, Jobcategory
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from dotenv import dotenv_values
from django.conf import settings
import os 
config = dotenv_values(".env")

# if not  settings.DEBUG else config["FASTAPIURL"]
@shared_task()
def stackoverflow_scrapper():
    res = requests.get(f'http://{os.environ.get("FASTAPIURL")}/scrape-stackoverflow',verify=False)
    return res.text
