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


def basket(request):
    template = loader.get_template("delivery/basket.html")
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template("delivery/contact.html")
    return HttpResponse(template.render())


def feedback(request):

    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phoneNumber")
        email = request.POST.get("email")
        message = request.POST.get("message")

        feedback = Users.objects.create(
            name=name, phone_number=phone_number, email=email, message=message
        )
        return HttpResponseRedirect("/main_page/")
    return render(request, "delivery/index.html")
