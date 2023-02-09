
from collections import UserList
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,permissions,authentication
from .models import Fooditems,Activityitems,UserFooditems,UserActivityitems
from .serializers import Fooditemserializer,Activityitemserializer,userActivityserializer,userFoodserializer,UserModel
# Create your views here.


# food items can all displayed and add an item admin side 
class Additems(APIView):
    def get(self,request,*agrs,**kagrs):
        all_items= Fooditems.objects.all()
        serializer=Fooditemserializer(all_items,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kagrs):
        serializer=Fooditemserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            all_items= Fooditems.objects.all()
            serializer=Fooditemserializer(all_items,many=True)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
# Activity listed in user then admin is approved section

class AproveActivity(APIView):
    def get(self,request,*agrs,**kagrs):
        id=kagrs.get("id")
        Activity_item=UserActivityitems.objects.get(id=id)
        Activityitems.objects.create(activity_name=Activity_item.activity_name,min=Activity_item.min,calorie=Activity_item.calorie).save()
        UserActivityitems.objects.get(id=id).delete()
        all_items= Activityitems.objects.all()
        serializer=Activityitemserializer(all_items,many=True)
        return Response(data=serializer.data)
# food items listed in user then admin is approved section

class AproveItem(APIView):
    def get(self,request,*agrs,**kagrs):
        id=kagrs.get("id")
        Activity_item=UserFooditems.objects.get(id=id)
        Fooditems.objects.create(food_name=Activity_item.food_name,food_type=Activity_item.food_type,protein=Activity_item.protein,qty=Activity_item.qty,calorie=Activity_item.calorie).save()
        UserFooditems.objects.get(id=id).delete()
        all_items= Fooditems.objects.all()
        serializer=Fooditemserializer(all_items,many=True)
        return Response(data=serializer.data)
    # def delete(self,request,*agrs,**kagrs):
    #     id=kagrs.get("id")
    #     UserFooditems.objects.get(id=id).delete()
    #     all_items= UserFooditems.objects.all()
    #     serializer=UserAdditems(all_items,many=True)
    #     return Response(data=serializer.data)
    
# food items can all displayed and add an activity user side but not add main list

class UserAdditems(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*agrs,**kagrs):
        all_items= UserFooditems.objects.all()
        serializer=userFoodserializer(all_items,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kagrs):
        serializer=userFoodserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            all_items= UserFooditems.objects.all()
            serializer=userFoodserializer(all_items,many=True)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# Activity can all displayed and add an item user side but not add main list

class UserAddActivity(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*agrs,**kagrs):
        all_items= UserActivityitems.objects.all()
        serializer=userActivityserializer(all_items,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kagrs):
        serializer=userActivityserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            all_items= UserActivityitems.objects.all()
            serializer=userActivityserializer(all_items,many=True)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
# activity can all displayed and add an activity admin side 

class Addactivity(APIView):
    def get(self,request,*agrs,**kagrs):
        all_items= Activityitems.objects.all()
        serializer=Activityitemserializer(all_items,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kagrs):
        serializer=Activityitemserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            all_items= Activityitems.objects.all()
            serializer=Activityitemserializer(all_items,many=True)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# to calcualte calories and protein week,month,day,and qty
class Caloriescalc(APIView):
    permission_classes=[permissions.IsAuthenticated]
    
    def get(self,request,*agrs,**kagrs):
        id=kagrs.get("id")
        Activity_item=Fooditems.objects.get(id=id)
        # print(Activity_item)
       
        if "day" in request.query_params and "qty" in request.query_params:
            qty= int(request.query_params.get("qty"))
            day= int(request.query_params.get("day"))
            calories = int(Activity_item.calorie) * (qty/ Activity_item.qty) * day
            protein = float(Activity_item.protein) * (qty/ Activity_item.qty) * day
            print(calories)
            return Response(data={"protein":protein,"calories":calories})
        if "week" in request.query_params and "qty" in request.query_params:
            week= int(request.query_params.get("week"))
            qty= int(request.query_params.get("qty"))
            calories = int(Activity_item.calorie) * (qty/ Activity_item.qty) *(week *7)
            protein = float(Activity_item.protein) * (qty/ Activity_item.qty) *(week *7)
            return Response(data={"protein":protein,"calories":calories})
        if "month" in request.query_params and "qty" in request.query_params:
            month= int(request.query_params.get("month"))
            qty= int(request.query_params.get("qty"))
            calories = int(Activity_item.calorie) * (qty/ Activity_item.qty) *(month * 30)
            protein = float(Activity_item.protein) * (qty/ Activity_item.qty) *(month * 30)
            return Response(data={"protein":protein,"calories":calories})
        if "qty" in request.query_params:
            qty= int(request.query_params.get("qty"))
            calories = int(Activity_item.calorie) * (qty/ Activity_item.qty)
            protein = float(Activity_item.protein) * (qty/ Activity_item.qty)
            return Response(data={"protein":protein,"calories":calories})
        return Response(data={"protein":Activity_item.protein,"calories":Activity_item.calorie})

# to calcualte calories burnout week,month,day,and min
class Acitivitycalc(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*agrs,**kagrs):
        id=kagrs.get("id")
        Activity_item=Activityitems.objects.get(id=id)
        # print(Activity_item)
    #    enter only minutes 
        if "day" in request.query_params and "min" in request.query_params:
            min= int(request.query_params.get("min"))
            day= int(request.query_params.get("day"))
            calories = int(Activity_item.calorie) * (min/ Activity_item.min) * day
            return Response(data={"calories burnout":calories})
        if "week" in request.query_params and "min" in request.query_params:
            week= int(request.query_params.get("week"))
            min= int(request.query_params.get("min"))
            calories = int(Activity_item.calorie) * (min/ Activity_item.min) *(week *7)
            return Response(data={"calories burnout":calories})
        if "month" in request.query_params and "min" in request.query_params:
            month= int(request.query_params.get("month"))
            min= int(request.query_params.get("min"))
            calories = int(Activity_item.calorie) * (min/ Activity_item.min) *(month * 30)
            return Response(data={"calories burnout":calories})
        if "min" in request.query_params:
            min= int(request.query_params.get("min"))
            calories = int(Activity_item.calorie) * (min/ Activity_item.min)
            return Response(data={"calories burnout":calories})
        return Response(data={"calories burnout":Activity_item.calorie})




# register users
class Signup(APIView):
    def post(self,request,*args,**kwargs):
        serial=UserModel(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data)
        else:
            return Response(data=serial.errors)