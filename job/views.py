from urllib import request
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .models import *
from job.serializers import *
from rest_framework.generics import * 
from rest_framework.permissions import  IsAuthenticated
from rest_framework import filters
# Create your views here.


# create job ad
class JobApiCreate(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)
    

# job ad list
class JobApiList(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

# job ad detail
class JobApiDetail(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
# see jobs created
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def jobs_created(request):
    jobs = Job.objects.filter(user=request.user)
    jobs_serializer = JobSerializer(jobs , many = True)
    return Response(jobs_serializer.data)


# job edit or update
class JobApiUpdate(RetrieveUpdateAPIView):
    def get_queryset(self):
        queryset = Job.objects.filter(user=self.request.user)
        return queryset
    
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)
    
    
# job edit or update
class JobApiDelete(RetrieveDestroyAPIView):
    def get_queryset(self):
        queryset = Job.objects.filter(user=self.request.user)
        return queryset
    
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)
    
    
    
    
# create request
class RequestApiCreate(CreateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)
    
    
    
# requests was sent for job
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def requests_sent(request,pk):
    requests = RequestModel.objects.filter(job=pk).filter(user=request.user)
    requests_serializer = RequestSerializer(requests , many = True)
    return Response(requests_serializer.data)


# create skill
class SkillApiCreate(CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAuthenticated,)
    
