# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.generics import (
 ListAPIView,
 CreateAPIView,
 RetrieveAPIView,
 )
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK , HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .models import Userdetails
from .serializers import (
  UserdetailsSerializer,
  UserCreateSerializer,
  UserDetailSerializer,
  UserLoginSerializer,
  )
from rest_framework.permissions import (
 AllowAny,
 IsAuthenticated,
 IsAdminUser,
 IsAuthenticatedOrReadOnly,
 )


# Create your views here.
class UserCreateView(CreateAPIView):
  queryset = Userdetails.objects.all()
  serializer_class = UserCreateSerializer
  
class UserDetailView(RetrieveAPIView):
  queryset = Userdetails.objects.all()
  serializer_class = UserDetailSerializer

  
class UserListView(ListAPIView):
  queryset = Userdetails.objects.all()
  serializer_class = UserdetailsSerializer
  
  
class UserLoginView(APIView):
  permission_classes = [IsAuthenticatedOrReadOnly]
  serializer_class = UserLoginSerializer

  def post(self,request,*args,**kwargs):
   data = request.data
   serializer = UserLoginSerializer(data=data)
   if serializer.is_valid(raise_exception=True):
	 new_data = serializer.data
	 return Response(new_data,status=HTTP_200_OK)
   return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
