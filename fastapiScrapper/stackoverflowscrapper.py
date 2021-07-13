from bs4 import BeautifulSoup
import requests
from icecream import ic
import aiohttp
import time
from models import Jobs, JobCategory


async def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


async def extract_job(html, name, url):
    ic()
    soup = html.find("div", {"class": "fl1"})
    title = soup.find("h2").find("a")["title"]
    link = soup.find("h2").find("a")["href"]
    companies, locations = soup.find("h3").find_all("span", recursive=False)
    # recursive all for only 2 spans to avoid going deeper spans
    company = companies.get_text(strip=True).strip(" \r").strip("\n")
    location = locations.get_text(strip=True).strip(" \r").strip("\n")
    """ try and except are only for error handling because in async
     the tortoise orm get_or_create method can return 2 or more object and 
     causing the program to fail"""
    try:
        ic()
        await Jobs.get_or_create(
            title=title,
            company_name=company,
            location=location,
            jobCategory=name,
            link=url + link,
            job_by="stackoverflow",
        )
    except Exception as e:
        print(e)
        pass


async def extract_jobs(last_page, url, name):
    jobs = []
    print(f"geting data for {name}")
    async with aiohttp.ClientSession() as session:
        for page in range(1, last_page):
            async with session.get(f"{url}&pg={page}") as resp:
                result = await resp.text()
                soup = BeautifulSoup(result, "html.parser")
                results = soup.find_all("div", {"class": "-job"})
                for resul in results:
                    job = await extract_job(resul, name, url)
                    jobs.append(job)
        return jobs
