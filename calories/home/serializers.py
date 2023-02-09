from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Fooditems,Activityitems,UserActivityitems,UserFooditems

class Fooditemserializer(serializers.ModelSerializer):
    class Meta:
        model=Fooditems
        fields="__all__"

class Activityitemserializer(serializers.ModelSerializer):
    class Meta:
        model=Activityitems
        fields="__all__"

class userFoodserializer(serializers.ModelSerializer):
    class Meta:
        model=UserFooditems
        fields="__all__"

class userActivityserializer(serializers.ModelSerializer):
    class Meta:
        model=UserActivityitems
        fields="__all__"


# user section
class UserModel(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)