from django.db import models

# Create your models here.


class Restaurant(models.Model):
    STATUS_CHOICES = [
        ('открыто', 'Открыто'),
        ('закрыто', 'Закрыто')
    ]

    name_restaurant = models.CharField(max_length=240)
    address = models.CharField(max_length=240)
    start_date = models.DateField()
    end_date = models.DateField()
    img_restaurant = models.CharField(max_length=254)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='закрыто')

    def __str__(self):
        return self.name_restaurant

    class Meta:
        db_table = 'restaurant'
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'
        ordering = ['status']


class Categories(models.Model):
    name_category = models.CharField(max_length=160)

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'catefories'

    def __str__(self):
        return self.name_category


class MenuItems(models.Model):
    name_item = models.CharField(max_length=240)
    price = models.CharField(max_length=240)
    quantity = models.IntegerField()
    info = models.TextField()
    restaurant = models.ManyToManyField(Restaurant)


    class Meta:
        db_table = 'menu_items'
        verbose_name = 'menu_item'
        verbose_name_plural = 'menu_items'

    def __str__(self):
        return self.name_item


class ImgItems(models.Model):
    img_item = models.CharField(max_length=255)
    menu_item = models.ManyToManyField(MenuItems)

    class Meta:
        db_table = 'img_items'
        verbose_name = 'img_item'
        verbose_name_plural = 'img_items'

    def __str__(self):
        return self.img_item


class Orders(models.Model):
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=140)
    price = models.CharField(max_length=255)
    quantity = models.IntegerField()
    order_date = models.DateField()

    class Meta:
        db_table = 'orders'
        verbose_name = 'order'
        verbose_name_plural = 'orders'




