from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path("addtocart/",cart,name="cart"),
    path("addtocard/<int:pk>",addtocard,name='addtocard'),
 
   ]
    