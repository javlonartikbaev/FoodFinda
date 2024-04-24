
from django.contrib import admin
from django.urls import path
from adminPanel import views as admin_views
from delivery import views as delivery_views


urlpatterns = [
    path("adminPanel/", admin_views.index, name="adminPanel"),
    path("adminPanel/menu_items", admin_views.get_menu_items, name="menu_items"),

    path("adminPanel/<slug:item_slug>/", admin_views.update_item, name="admin_update_items"),
]
