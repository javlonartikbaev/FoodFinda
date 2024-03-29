from django.contrib import admin
from .models import *
# Register your models here.


class AdminRestaurant(admin.ModelAdmin):
    list_display = ('name_restaurant', 'address','start_date','end_date', 'img_restaurant','status')


class AdminCategories(admin.ModelAdmin):
    list_display = ('name_category',)


class AdminMenuItem(admin.ModelAdmin):
    list_display = ('name_item','price', 'quantity', 'info')


admin.site.register(MenuItems, AdminMenuItem)
admin.site.register(Categories, AdminCategories)
admin.site.register(Restaurant,AdminRestaurant)