from rest_framework import serializers
from django.contrib.humanize.templatetags import humanize
from .models import Jobs, Jobcategory



class JobsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobcategory
        fields = ['name']


class JobsSerializer(serializers.ModelSerializer):
    jobcategory = JobsCategorySerializer(read_only=True, many=False)
    create_at = serializers.SerializerMethodField('get_date')
    def get_date(self, obj):
        return humanize.naturaltime(obj.created_at)
    class Meta:
        model = Jobs
        fields = ['title', 'rating', 'location', 'company_name',
                  'create_at', 'jobcategory', 'id', 'link', 'job_by']
