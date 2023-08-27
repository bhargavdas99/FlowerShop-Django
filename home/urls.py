from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('decoration',views.about,name="decoration"),
    path('gift',views.about,name="gift"),
    path('bouquet',views.about,name="bouquet")
]