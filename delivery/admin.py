from django.contrib import admin
from .models import *


class AdminRestaurant(admin.ModelAdmin):
    list_display = (
        "name_restaurant",
        "address",
        "start_time",
        "end_time",
        "img_restaurant",
        "status",
        "restaurant_slug",
    )


class AdminCategories(admin.ModelAdmin):
    list_display = ("name_category", "img_category", "category_slug")


class AdminMenuItem(admin.ModelAdmin):
    list_display = (
        "name_item",
        "price",
        "quantity",
        "info",
        "restaurant",
        "category",
        "menu_slug",
    )


class AdminImgItems(admin.ModelAdmin):
    list_display = ("img_item", "menu_item_id")


class AdminBaskets(admin.ModelAdmin):
    list_display = ("menu_items", "price", "quantity")


class AdminOrders(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "phone",
        "total_price",
        "status",
    )


class AdminUsersFeedback(admin.ModelAdmin):
    list_display = ("name", "phoneNumber", "email", "message")


admin.site.register(Restaurant, AdminRestaurant)
admin.site.register(Categories, AdminCategories)
admin.site.register(MenuItems, AdminMenuItem)
admin.site.register(ImgItems, AdminImgItems)
admin.site.register(Basket, AdminBaskets)
admin.site.register(Orders, AdminOrders)
admin.site.register(Users, AdminUsersFeedback)
