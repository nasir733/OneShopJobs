from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator


class JobCategory(Model):
    name = fields.CharField(max_length=244, unique=True)

    def __str__(self):
        return self.name

    class PydanticMeta:
        pass


JobCategory_Pydantic = pydantic_model_creator(JobCategory, name="JobCategory")
JobCategoryIn_pydantic = pydantic_model_creator(
    JobCategory, name="JobCategoryIn")


class Jobs(Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = fields.CharField(max_length=255, null=True)
    company_name = fields.CharField(max_length=255, null=True)
    location = fields.CharField(max_length=255, null=True)
    rating = fields.CharField(max_length=255, null=True)
    created_at = fields.data.DatetimeField(auto_now_add=True)
    jobCategory = fields.relational.ForeignKeyField(
        "models.JobCategory", on_delete=fields.SET_NULL, null=True, blank=True
    )
    link = fields.CharField(max_length=11250, blank=True, null=True)
    job_by = fields.CharField(max_length=255, blank=True, null=True)

    class PydanticMeta:
        pass


Jobs_Pydantic = pydantic_model_creator(Jobs, name="Jobs")
JobsIn_pydantic = pydantic_model_creator(Jobs, name="JobsIn")
