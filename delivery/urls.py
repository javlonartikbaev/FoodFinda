"""
URL configuration for delivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from delivery.views import *
from delivery import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main_page, name="main_page"),
    path("basket/", views.basket, name="basket"),
    path("categories/", views.categories, name="categories"),
    path("contact/", views.contact, name="contact"),
    path("restaurants/", views.restaurants, name="restaurants"),
    path(
        "restaurants/<slug:restaurant_slug>",
        views.selected_restaurant,
        name="selected_restaurant",
    ),
    path("menu_items/<slug:item_slug>/", views.menu_items, name="menu_items"),
]
