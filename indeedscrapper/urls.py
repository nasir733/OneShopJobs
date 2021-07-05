from django.urls import path, include
from .views import  JobsViewSet, Jobscategory
from rest_framework import routers

router = routers.SimpleRouter()
router.register("jobs", JobsViewSet)
router.register("jobnames", Jobscategory)
urlpatterns = [
    # path("", startScrapper),
]
urlpatterns += router.urls
