
from django.contrib import admin
from django.urls import path
from adminPanel import views as admin_views
from delivery import views as delivery_views


urlpatterns = [
    path("adminPanel/", admin_views.index, name="adminPanel"),
    path("adminPanel/menu_items", admin_views.get_menu_items, name="menu_items"),
    path("adminPanel/addItem/", admin_views.add_item, name="admin_add_item"),
    path("adminPanel/<slug:item_slug>/", admin_views.update_item, name="admin_update_items"),
    path("adminPanel/<slug:item_slug>/delete", admin_views.delete_item, name="admin_delete_item"),
]