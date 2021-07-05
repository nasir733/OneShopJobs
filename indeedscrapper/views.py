from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from rest_framework import viewsets
from .serializers import JobsSerializer, JobsCategorySerializer
from bs4 import BeautifulSoup
from pprint import pprint
from .models import Jobs, JobCategory
from asgiref.sync import sync_to_async

list_of_jobs = []
NUM_OF_PAGES = 2


def get_number_of_jobs(soup):
    count_pages = soup.find(id="searchCountPages").text.strip()
    count_pages_list = count_pages.split(" ")
    num_job_str = count_pages_list[3].replace(",", "")
    num_jobs = int(num_job_str)
    # Number of Jobs
    print(f"Number of Jobs: {num_jobs} ")


def get_next_page(soup):
    pagination = soup.find("ul", class_="pagination-list")
    pages = pagination.find_all("li")
    last_page = pages[-1].find("a")["href"]
    next_page = f"https://www.indeed.com{last_page}"
    return next_page


def get_jobs(soup):
    # list of jobs
    job_list = soup.find_all("div", class_="jobsearch-SerpJobCard")
    for job in job_list:
        title = job.find("a", class_="jobtitle").text.strip()
        company_name = job.find("span", class_="company").text.strip()
        location = job.find("span", class_="location")
        rating = job.find("span", class_="ratingsContent")
        if location:
            location = location.text.strip()
        if rating:
            rating = rating.text.strip()
        job_dict = {
            "title": title if title else None,
            "company_name": company_name if company_name else None,
            "location": location if location else None,
            "rating": rating if rating else None,
        }
        Jobs.objects.get_or_create(
            title=title, company_name=company_name, location=location, rating=rating
        )
        list_of_jobs.append(job_dict)


def loop_through_pages(names):
    for name in names:
        URL = f"https://www.indeed.com/jobs?q={name}t&l="
        current_page = 0
        while current_page < NUM_OF_PAGES and URL:
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            print("Loading:", URL)
            get_jobs(soup)
            URL = get_next_page(soup)
            current_page += 1


# get_number_of_jobs(soup)
# get_next_page(soup)
# get_jobs(soup)
# how do we loop through the first 10 pages and get all of the jobs
# loop_through_pages()
print(len(list_of_jobs))
pprint(list_of_jobs)
# Create your views here.


# @sync_to_async
# async def startScrapper(request):
#     jobsName = JobCategory.objects.all()
#     print(jobsName)
#     for jobs in jobsName:
#         print(jobs)
#     loop_through_pages(jobsName)
#     return HttpResponse(list_of_jobs)


class Jobscategory(viewsets.ModelViewSet):
    queryset = JobCategory.objects.all()
    pagination_class = None

    serializer_class = JobsCategorySerializer
    lookup_field = "name"
    permission_classes = []


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.order_by("-created_at")
    serializer_class = JobsSerializer
    lookup_field = "jobCategory"
    permission_classes = []
    search_fields = (
        "rating",
        "location",
        "title",
        "company_name",
        "created_at",
        "job_by",
        "jobCategory",
    )
    ordering_fields = ["rating", "location", "created_at", "jobCategory"]
