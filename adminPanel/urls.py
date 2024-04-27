from django.contrib import admin
from django.urls import path
from adminPanel import views as admin_views
from delivery import views as delivery_views

urlpatterns = [
    path("adminPanel/", admin_views.index, name="adminPanel"),
    path("adminPanel/menu_items", admin_views.get_menu_items, name="menu_items"),
    path('adminPanel/feedback', admin_views.users_feedback, name="users_feedback"),
    path('adminPanel/img_item', admin_views.imgItem, name="admin_img_item"),
    path('adminPanel/admin-basket', admin_views.admin_basket, name="admin_basket"),
    path('adminPanel/orders', admin_views.admin_orders, name="admin_orders"),
    path('adminPanel/logIn', admin_views.logIn, name="logIn"),

    path('adminPanel/<int:id_orders>/', admin_views.updateOrders, name="update_orders"),
    path("adminPanel/addItem/", admin_views.add_item, name="admin_add_item"),
    path("adminPanel/addImgItem/", admin_views.add_img_item, name="admin_add_img_item"),
    path("adminPanel/<slug:item_slug>/", admin_views.update_item, name="admin_update_items"),

    path('adminPanel/<int:img_item_id>/delete', admin_views.delete_img_item, name="admin_del_img_item"),
    path("adminPanel/<slug:item_slug>/delete", admin_views.delete_item, name="admin_delete_item"),
    path('adminPanel/<slug:category_slug>/delete_categories', admin_views.delete_categories,
         name="admin_delete_categories"),
    path('adminPanel/categories', admin_views.admin_categories, name="admin_categories"),

    path('adminPanel/addCategories', admin_views.add_admin_categories, name="add_admin_categories"),


    path('adminPanel/<slug:category_slug>', admin_views.update_admin_categories, name="admin_categories"),



]
