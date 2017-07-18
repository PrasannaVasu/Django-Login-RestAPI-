from rest_framework.serializers import ModelSerializer

from .models from Userdetails

class UserdetailsSerializer(ModelSerializer):
  class Meta:
    model = Userdetails
	field = [
       'username',
	   'password',
	   'email',
	   'comment',
       'publish',	   
	]