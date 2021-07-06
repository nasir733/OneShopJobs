from django.contrib import admin
from . import models
from django.utils.html import mark_safe

# Register your models here.
# admin.site.register(models.Jobs)
admin.site.register(models.Jobcategory)


@admin.register(models.Jobs)
class JobAdmin(admin.ModelAdmin):
    """Jobs Admin Definition"""

    list_display = (
        "title",
        "company_name",
        "jobcategory",
        "location",
        "job_by",
        "link",
        # "job_link",
    )
    list_filter = ("jobcategory", "job_by")

    def job_link(self, obj):
        return mark_safe(
            f'<a style="position-relative;" href="{obj.link}>Link to the job</a>'
        )