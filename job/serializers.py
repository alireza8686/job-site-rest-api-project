from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = '__all__'
        
        
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'