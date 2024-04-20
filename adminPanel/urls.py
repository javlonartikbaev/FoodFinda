
from django.contrib import admin
from django.urls import path
from adminPanel import views

urlpatterns = [
    path("adminPanel/", views.index, name="adminPanel"),

]
