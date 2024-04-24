from django.shortcuts import render, get_object_or_404, redirect
from delivery.models import *
# Create your views here.
from adminPanel.forms import *


def index(request):
    return render(request, 'adminPanel/index.html')


def get_menu_items(request):
    menu_items = MenuItems.objects.all()
    data = {"menu_items": menu_items}
    return render(request, 'adminPanel/index.html', data)


def admin_menu_items(request, item_slug):
    menu_items = get_object_or_404(MenuItems, menu_slug=item_slug)
    data = {"menu_items": menu_items}
    return render(request, "adminPanel/AdminUpdateMenuItems.html", data)


def update_item(request, item_slug):
    item = get_object_or_404(MenuItems, menu_slug=item_slug)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu_items')
    else:
        form = MenuItemForm(instance=item)
    return render(request, "adminPanel/AdminUpdateMenuItems.html", {'form': form})
