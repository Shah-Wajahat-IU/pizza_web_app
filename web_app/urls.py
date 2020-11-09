
from django.contrib import admin
from django.urls import path
from .views import adminloginview,homepage,authenticateadmin

urlpatterns = [
    path('admin/',adminloginview , name='userlogin'),
    path('authenticate/',authenticateadmin),
     path('admin/home',homepage, name='homepage'),
]
