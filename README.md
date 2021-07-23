
# OneShopJobs

The aim of this website is to provide user a single place to find all the jobs from there favourite Job websites
in one place you can visit the app at https://oneshopjobs.herokuapp.com/
## Demo
### Demo Credientials :-
#### username = demo1 , Password=ultimatedemo
https://oneshopjobs.herokuapp.com/

  
## Tech Stack:-

### Frontend
**Client:** 
- Django-Templates
- Vanilla-Js 
- HTML-5
- TailwindCSS

### Backend 
**Server:**
- Django ( Allauth , Django-Rest-Framework , Django-Extensions,django-cors-headers , Django-Clerey-Beat , Celery , Redis , Postgresql )
- Scrapper ( Aiohttp, Asyncio, Icecream , BeautifullSoup4 )
- fastapi ( Tortoise-Orm , Cors, Postgresql )

  
## Features

### Backend
#### In the backend iam using a microservice architecture  in which Django is my main server which handles all the user reqeust and serving the api where the fastapi is to run my webscrappers . Iam using celery to schedule the task to ping my fastapi server every 5-10mins to run the scrapper. the django server is hosting the main [api](https://oneshopjobs.herokuapp.com/api/v1/jobs/) that our frontend is consuming you can see the more detail about the api at the [Redocs](https://oneshopjobs.herokuapp.com/api/schema/redoc/) 

### Scrapper 
#### I am using fastapi to host my scrapper these are not the normal webscrappers that you might have seen in the past this scrapper can scrape the whole stackoverflow jobs section in just 36 seconds and store the results in the database to achieve thses kind of results we are using aiohttp instead of the normal reqeusts library for accessing the web page of the  stackoverflow because aiohttp is an async library the scrapper are async concurent scrappers which means that they fire the reqeusts to all the 9 pages of the stackoverflow at once so all the data is bieng scrapped at the same time this is possible due to the awesome library asyncio  function called [asyncio.ensurefuture()](https://docs.python.org/3/library/asyncio-task.html) you can read more about it at [python docs](https://docs.python.org/3/library/asyncio-task.html)

### Frontend 
#### The frontend is built using the HTMl5-Tailwindcss and Vanilla js the frontend is consuming our backend django api api 
- Sign-in 
- Registeraion
- log-out 
- Infinite Scroll Pagination
- searching / filtering 
- responsive 
## Backend 

#### Get all Jobs

```http
  GET /api/v1/jobs/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get all the job categorys and post a new job category

```http
  GET /api/v1/jobnames/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |



  