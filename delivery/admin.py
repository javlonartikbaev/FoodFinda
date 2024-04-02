from django.contrib import admin
from .models import *
# Register your models here.


class AdminRestaurant(admin.ModelAdmin):
    list_display = ('name_restaurant', 'address','start_date','end_date', 'img_restaurant','status')


class AdminCategories(admin.ModelAdmin):
    list_display = ('name_category',)


class AdminMenuItem(admin.ModelAdmin):
    list_display = ('name_item', 'price', 'quantity', 'info', 'restaurant','category')

class AdminImgItems(admin.ModelAdmin):
    list_display = ('img_item', )

class AdminBaskets(admin.ModelAdmin):
    list_display = ('menu_items',)

class AdminOrders(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'price', 'quantity', 'status')

class AdminUsersFeedback(admin.ModelAdmin):
    list_display = ('name', 'phoneNumber', 'email', 'message')


admin.site.register(Restaurant,AdminRestaurant)
admin.site.register(Categories, AdminCategories)
admin.site.register(MenuItems, AdminMenuItem)
admin.site.register(ImgItems, AdminImgItems)
admin.site.register(Basket, AdminBaskets)
admin.site.register(Orders, AdminOrders)
admin.site.register(Users, AdminUsersFeedback)