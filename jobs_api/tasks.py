
from celery import shared_task

# from celery.decorators import periodic_task
# from celery.task.schedules import crontab
from .models import Jobs, Jobcategory
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from dotenv import dotenv_values
config = dotenv_values(".env")


@shared_task()
def stackoverflow_scrapper():
    res = requests.get(f'http://{config["FASTAPIURL"]}/scrape-stackoverflow',verify=False)
    return res.text
