from dataclasses import field
from django.shortcuts import render
from rest_framework.generics import * 
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from rest_framework.permissions import  IsAuthenticated


# Create your views here.


class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InformationCreateApiView(CreateAPIView):
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationSerializer



class InformationApiView(RetrieveAPIView):
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationSerializer
    
    
    
class InformationApiUpdate(RetrieveUpdateAPIView):
    def get_queryset(self):
        queryset = UserInformation.objects.filter(user=self.request.user)
        return queryset
    
    serializer_class = UserInformationSerializer
    permission_classes = (IsAuthenticated,)