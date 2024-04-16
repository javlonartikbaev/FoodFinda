from tkinter import Menu

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *

# templates


def main_page(request):
    categories = Categories.objects.all()
    restaurants = Restaurant.objects.all()
    context = {"categories": categories, "restaurants": restaurants}
    return render(request, "delivery/index.html", context)


def categories(request):
    categories = Categories.objects.all()
    context = {"categories": categories}
    return render(request, "delivery/categories.html", context)


def restaurants(request):
    restaurants = Restaurant.objects.all()
    context = {"restaurants": restaurants}
    return render(request, "delivery/restaurants.html", context)


def selected_restaurant(request, restaurant_slug):
    restaurant = get_object_or_404(Restaurant, restaurant_slug=restaurant_slug)
    menu_items = MenuItems.objects.filter(restaurant=restaurant)
    categories = Categories.objects.filter(restaurant_id=restaurant.id)

    context = {
        "restaurant": restaurant,
        "menu_items": menu_items,
        "categories": categories,
    }
    return render(request, "delivery/menu_items.html", context)


def basket(request):
    template = loader.get_template("delivery/basket.html")
    return HttpResponse(template.render())


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Users.objects.create(
            name=name, phoneNumber=phone_number, email=email, message=message
        )
        return HttpResponseRedirect("/")
    return render(request, "delivery/contact.html")


def menu_items(request, item_slug):
    items = get_object_or_404(MenuItems, slug=item_slug)
    data = {"menu_items": items}
    return render(request, "delivery/menu_items.html", data)
