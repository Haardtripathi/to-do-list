from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('delete-task/<int:id>/',DeleteTask,name="delete"),
    path('update/<int:id>/',Update,name="update"),

]
