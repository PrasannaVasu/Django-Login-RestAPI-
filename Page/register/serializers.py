from rest_framework import serializers

from .models import Userdetails
from django.db.models import Q
from rest_framework.serializers import (
  CharField,
  ValidationError,
  )
  
import django.contrib.auth.password_validation as validators




class UserdetailsSerializer(serializers.ModelSerializer):
 class Meta:
   model = Userdetails
   fields = [
       'username',
	   'email',
	   'comments',
       'publish',	   
	]
	
class UserCreateSerializer(serializers.ModelSerializer):
  username = serializers.CharField()
  password = serializers.CharField(write_only=True)
  class Meta:
   model = Userdetails
   fields = [
     'username',
	 'password',
	 'email',
	 'comments',
	 'publish',
   ]
   
class UserDetailSerializer(serializers.ModelSerializer):
  username = serializers.CharField()
  class Meta:
   model = Userdetails
   fields = [
     'username',
	 'comments',
	 'publish',
   ]

  def validate(self , data):
   
    return data
   	 
	 
class UserLoginSerializer(serializers.ModelSerializer):
  username = CharField(required=False,allow_blank=True)
  class Meta:
   model = Userdetails
   fields = [
     'username',
	 'password',
	 
   ]
   
  def validate(self , data):
   user_obj = None
   username = data.get("username",None)
   password = data.get("password")
   if not username:
    raise  ValidationError("A username is required to login.")
   
   user = Userdetails.objects.filter(
            Q(username=username) ,
			Q(password=password)
			).distinct()
   print user
   if user.exists() and user.count()==1:
    user_obj = user.first()
   else:
    raise ValidationError("This username is not valid.")
	
   #if user_obj:
    #if not user_obj.check_password(password):
     #raise ValidationError("Incorrect credentials please try again.")
	 
   return data
  