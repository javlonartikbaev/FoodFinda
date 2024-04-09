from django.db import models
from datetime import datetime

# Create your models here.


class Restaurant(models.Model):
    STATUS_CHOICES = [("открыто", "Открыто"), ("закрыто", "Закрыто")]

    name_restaurant = models.CharField(max_length=240)
    address = models.CharField(max_length=240)
    start_time = models.TimeField(default=datetime.now)
    end_time = models.TimeField(default=datetime.now)
    img_restaurant = models.ImageField(upload_to="delivery/img/", default="")
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="закрыто")

    def __str__(self):
        return self.name_restaurant

    class Meta:
        db_table = "restaurant"
        verbose_name = "restaurant"
        verbose_name_plural = "restaurants"
        ordering = ["-status"]


class Categories(models.Model):
    name_category = models.CharField(max_length=160)
    img_category = models.ImageField(upload_to="delivery/img_category/", default="")

    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name_category


class MenuItems(models.Model):
    name_item = models.CharField(max_length=240)
    price = models.CharField(max_length=240)
    quantity = models.IntegerField(null=False, blank=True)
    info = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default="")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default="")

    class Meta:
        db_table = "menu_items"
        verbose_name = "menu_item"
        verbose_name_plural = "menu_items"

    def __str__(self):
        return self.name_item


class ImgItems(models.Model):
    img_item = models.ImageField(upload_to="delivery/img_items/img/", default="")
    menu_item_id = models.ForeignKey(MenuItems, on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = "img_items"
        verbose_name = "img_item"
        verbose_name_plural = "img_items"

    def __str__(self):
        return self.menu_item_id.name_item


class Basket(models.Model):
    menu_items = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = "basket"
        verbose_name = "basket"
        verbose_name_plural = "baskets"


class Orders(models.Model):
    STATUS_CHOICES = [
        ("в обработке", "В обработке"),
        ("В пути", "В пути"),
        ("доставлен", "Доставлен "),
        ("отменен ", "Отменен "),
    ]

    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=140)
    total_price = models.FloatField(default=0)
    order_date = models.DateField()
    status = models.CharField(
        choices=STATUS_CHOICES, max_length=100, default="в обработке"
    )
    basket = models.ManyToManyField(Basket)

    class Meta:
        db_table = "orders"
        verbose_name = "order"
        verbose_name_plural = "orders"


class Users(models.Model):
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField(max_length=450)

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"
