from operator import mod
from django.db import models

# Create your models here.

class Fooditems(models.Model):
    food_name=models.CharField(max_length=250)
    food_type=models.CharField(max_length=250)
    calorie=models.IntegerField()
    protein=models.FloatField()
    qty=models.IntegerField()

    def __str__(self):
        return self.food_name

class UserFooditems(models.Model):
    food_name=models.CharField(max_length=250)
    food_type=models.CharField(max_length=250)
    calorie=models.IntegerField()
    protein=models.FloatField()
    qty=models.IntegerField()

    def __str__(self):
        return self.food_name


class Activityitems(models.Model):
    activity_name=models.CharField(max_length=250)
    calorie=models.IntegerField()
    min=models.IntegerField()

    def __str__(self):
        return self.activity_name

class UserActivityitems(models.Model):
    activity_name=models.CharField(max_length=250)
    calorie=models.IntegerField()
    min=models.IntegerField()

    def __str__(self):
        return self.activity_name