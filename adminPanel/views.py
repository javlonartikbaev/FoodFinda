from django.shortcuts import render, get_object_or_404, redirect
from delivery.models import *
# Create your views here.
from adminPanel.forms import *
from django.core.paginator import Paginator
from django.shortcuts import render


def index(request):
    return render(request, 'adminPanel/index.html')


def get_menu_items(request):
    menu_items = MenuItems.objects.all().order_by('name_item')
    paginator = Paginator(menu_items, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"page_obj": page_obj}
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


def add_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_items')
    else:
        form = MenuItemForm()
    return render(request, 'adminPanel/AdminItemAdd.html', {"form": form})


def delete_item(request, item_slug):
    item = get_object_or_404(MenuItems, menu_slug=item_slug)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_items')

    return render(request, 'adminPanel/deleteItem.html', {'item': item})


def admin_categories(request):
    categories = Categories.objects.all()
    paginator = Paginator(categories, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"page_obj": page_obj}
    return render(request, 'adminPanel/adminCategories.html', data)


def update_admin_categories(request, category_slug):
    categories = get_object_or_404(Categories, category_slug=category_slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=categories)
        if form.is_valid():
            form.save()
            return redirect('admin_categories')
    else:
        form = CategoryForm(instance=categories)
    return render(request, 'adminPanel/updateCategories.html', {"form": form})


def add_admin_categories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            if 'img_category' in request.FILES:
                form.save()
                return redirect('admin_categories')
    else:
        form = CategoryForm()
    return render(request, 'adminPanel/addCategories.html', {"form": form})


def delete_categories(request, category_slug):
    category = get_object_or_404(Categories, category_slug=category_slug)
    if request.method == 'POST':
        category.delete()
        return redirect('admin_categories')

    return render(request, 'adminPanel/deleteCategories.html', {'category': category})


def users_feedback(request):
    users = Users.objects.all()
    paginator = Paginator(users, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"page_obj": page_obj}

    return render(request, 'adminPanel/UsersFeedback.html', data)


def imgItem(request):
    imgItems = ImgItems.objects.all()
    paginator = Paginator(imgItems, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"page_obj": page_obj}

    return render(request, 'adminPanel/AdminImgItem.html', data)


def delete_img_item(request, img_item_id):
    img_item = get_object_or_404(ImgItems, id=img_item_id)
    if request.method == 'POST':
        img_item.delete()
        return redirect('admin_img_item')
    return render(request, 'adminPanel/deleteImgItem.html', {'img_item': img_item})


def add_img_item(request):
    if request.method == 'POST':
        form = ItemImgForm(request.POST, request.FILES)
        if form.is_valid():
            if 'img_item' in request.FILES:
                form.save()
                return redirect('admin_img_item')
    else:
        form = ItemImgForm()
    return render(request, 'adminPanel/addImgItem.html', {"form": form})


def admin_basket(request):
    basket = Basket.objects.all()
    paginator = Paginator(basket, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"page_obj": page_obj}

    return render(request, 'adminPanel/adminBasket.html', data)


def admin_orders(request):
    orders = Orders.objects.all()
    paginator = Paginator(orders, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"page_obj": page_obj}

    return render(request, 'adminPanel/adminOrders.html', data)


def updateOrders(request, id_orders):
    order = get_object_or_404(Orders, id=id_orders)
    if request.method == 'POST':
        form = UpdateAdminForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin_orders')
    else:
        form = UpdateAdminForm(instance=order)
    return render(request, 'adminPanel/UpdateOrders.html', {"form": form})


def logIn(request):
    form = LogInForm()
    data = {'form': form}
    return render(request, 'adminPanel/logIn.html', data)
