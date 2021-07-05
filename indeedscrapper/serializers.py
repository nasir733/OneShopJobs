from rest_framework import serializers

from .models import Jobs,JobCategory
class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['title','rating','location','company_name','created_at','jobCategory','id','link','job_by']

class JobsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['name']