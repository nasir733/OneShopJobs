from celery import shared_task

# from celery.decorators import periodic_task
# from celery.task.schedules import crontab
from .models import Jobs, JobCategory
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from .StackOverFlowScrapper import extract_jobs
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
import asyncio
import requests

list_of_jobs = []
NUM_OF_PAGES = 1



def get_number_of_jobs(soup):
    count_pages = soup.find(id="searchCountPages").text.strip()
    count_pages_list = count_pages.split(" ")
    num_job_str = count_pages_list[3].replace(",", "")
    num_jobs = int(num_job_str)
    # Number of Jobs
    print(f"Number of Jobs: {num_jobs} ")


def get_next_page(soup):
    try:
        pagination = soup.find("ul", class_="pagination-list")
        pages = pagination.find_all("li")
        last_page = pages[-1].find("a")["href"]
        next_page = f"https://www.indeed.com{last_page}"
        return next_page
    except AttributeError:
        pass


def get_jobs(soup, name, URL):
    # list of jobs
    print("name---", name)
    try:
        job_list = soup.find_all("div", class_="jobsearch-SerpJobCard")
        for job in job_list:
            title = job.find("a", class_="jobtitle").text.strip()
            company_name = job.find("span", class_="company").text.strip()
            location = job.find("span", class_="location")
            rating = job.find("span", class_="ratingsContent")
            link = job.find("a")["href"]
            if location:
                location = location.text.strip()
            if rating:
                rating = rating.text.strip()
            # job_dict = {
            # "title":  title if title else None,
            # "company_name": company_name if company_name else None,
            # "location": location if location else None,
            # "rating": rating if rating else None,
            # "jobCategory":name,
            # }
            Jobs.objects.get_or_create(
                title=title,
                company_name=company_name,
                location=location,
                rating=rating,
                jobCategory=name,
                job_by="indeed",
                link="https://www.indeed.com" + link,
            )
            # list_of_jobs.append(job_dict)
    except requests.exceptions.ConnectionError or AttributeError:
        print("an exception happend")


# StackOverFlowScrapper
def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html, name, url):
    soup = html.find("div", {"class": "fl1"})
    title = soup.find("h2").find("a")["title"]
    link = soup.find("h2").find("a")["href"]
    companies, locations = soup.find("h3").find_all("span", recursive=False)
    # recursive all for only 2 spans to avoid going deeper spans
    company = companies.get_text(strip=True).strip(" \r").strip("\n")
    location = locations.get_text(strip=True).strip(" \r").strip("\n")
    Jobs.objects.get_or_create(
        title=title,
        company_name=company,
        location=location,
        jobCategory=name,
        link=url + link,
        job_by="stackoverflow",
    )


def extract_jobs(last_page, url, name):
    jobs = []
    print(f"geting data for {name}")
    for page in range(1, last_page):
        result = requests.get(f"{url}&pg={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for resul in results:
            job = extract_job(resul, name, url)
            jobs.append(job)
    return jobs

    # print(result.status_code)


@shared_task
def loop_through_pages():
    print("hello from indeed scrapper")
    jobsNamew = JobCategory.objects.all()
    for job in jobsNamew:
        URL = f"https://www.indeed.com/jobs?q={job}&limit=50"
        current_page = 0
        while current_page < NUM_OF_PAGES and URL:
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            print("Loading:", URL)
            get_jobs(soup, job, URL)
            URL = get_next_page(soup)
            current_page += 1


@shared_task()
def get_stackOverflow_jobs():
    print("hello from stackoverflow jobs section")
    jobsNames = JobCategory.objects.all()
    for job in jobsNames:


@shared_task()
def pingTheFastApiStackOverflowScrapper():
    pass