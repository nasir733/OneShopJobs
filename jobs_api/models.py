from django.db import models

# Create your models here.
class Jobcategory(models.Model):
    name = models.CharField(unique=True, max_length=244)
    def __str__(self):
        return self.name


    class Meta:
        managed = False
        db_table = 'jobcategory'


class Jobs(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    rating = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    link = models.CharField(max_length=11250, blank=True, null=True)
    job_by = models.CharField(max_length=255, blank=True, null=True)
    jobcategory = models.ForeignKey(Jobcategory, models.DO_NOTHING, db_column='jobCategory_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobs'