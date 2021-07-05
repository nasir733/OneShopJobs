from fastapi import FastAPI
from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from stackoverflowscrapper import extract_jobs
from fastapi.responses import JSONResponse
import time
import asyncio
from models import JobCategory, Jobs_Pydantic, Jobs
import uvicorn
app = FastAPI()


@app.get("/get-jobs")
async def getJobs():
    return await Jobs_Pydantic.from_queryset(Jobs.all())


@app.get("/create-category")
async def createCategory():
    return await JobCategory.create(name="Python")


@app.get("/")
async def startAsyncScrapper():
    print("hello from stackoverflow jobs section")

    actions = []
    start_time = time.time()
    jobsName = await JobCategory.all()
    print(jobsName)
    jobsNames = ['python', 'javascript', 'django', 'channels']
    # print(jobsName)
    for job in jobsName:
        url = f"https://stackoverflow.com/jobs?q={job}"
        actions.append(asyncio.ensure_future(extract_jobs(4, url, job)))
    await asyncio.gather(*actions)
    total_time = time.time() - start_time

    return 'hi my friend '


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
