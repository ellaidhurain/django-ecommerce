from products.models import Productdata,Customerdata,Order
from products.models import  User,Post
from rest_framework import serializers 
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User # custom model
      fields = "__all__"
      extra_kwargs = {
            'password':{
                'write_only': True
            }
        }


# create jwt  
class AccessTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # default
        token = super().get_token(user)

        # Add custom claims
        # this value is encrypted in token
        token['username'] = user.username
        # ...

        return token


class GroupUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        extra_kwargs = {
            'password':{
                'write_only': True
            }
        }


class ProductdataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productdata
        fields = '__all__'

class CustomerdataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customerdata
        fields = '__all__'

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'