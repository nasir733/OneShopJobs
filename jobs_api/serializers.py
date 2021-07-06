from rest_framework import serializers

from .models import Jobs, Jobcategory


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['title', 'rating', 'location', 'company_name',
                  'created_at', 'jobcategory', 'id', 'link', 'job_by']


class JobsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobcategory
        fields = ['name']
