from django.db import models

from django.db import models
import uuid

# Create your models here


class JobCategory(models.Model):
    name = models.CharField(max_length=244, unique=True)

    def __str__(self):
        return self.name


class Jobs(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    rating = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    jobCategory = models.ForeignKey(
        JobCategory, on_delete=models.SET_NULL, blank=True, null=True
    )
    link = models.CharField(max_length=11250, blank=True, null=True)
    job_by = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
