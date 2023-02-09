from django.urls import path
from .views import Additems,UserAdditems,AproveActivity,Addactivity,AproveItem,Caloriescalc,Acitivitycalc,UserAddActivity,Signup
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/calories/fooditems', Additems.as_view()),
    path('api/calories/Aproveitem/<int:id>',AproveItem.as_view()),
    path('api/calories/userlist', UserAdditems.as_view()),
    path('api/calories/activity', Addactivity.as_view()),
    path('api/calories/Aproveactivity/<int:id>',AproveActivity.as_view()),
    path('api/calories/Caloriescalc/<int:id>',Caloriescalc.as_view()),
    path('api/calories/Acitivitycalc/<int:id>',Acitivitycalc.as_view()),
    path('api/calories/UserAddActivity',UserAddActivity.as_view()),
    path('api/calories/Signup',Signup.as_view()),
    path('api/calories/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/calories/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
