from rest_framework import serializers

from .models import Jobs, Jobcategory



class JobsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobcategory
        fields = ['name']


class JobsSerializer(serializers.ModelSerializer):
    jobcategory = JobsCategorySerializer(read_only=True, many=False)
    class Meta:
        model = Jobs
        fields = ['title', 'rating', 'location', 'company_name',
                  'created_at', 'jobcategory', 'id', 'link', 'job_by']
