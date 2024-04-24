from django import forms
from delivery.models import MenuItems


# class MenuItemForm(forms.Form):
#
#     name_item = forms.CharField(label="Имя", max_length=100),
#     price = forms.CharField(label="Цена", max_length=100),
#     quantity = forms.CharField(label="Количество", max_length=100),
#     info = forms.CharField(label="Информация", max_length=100),
#     restaurant = forms.CharField(label="Ресторан", max_length=100),
#     category = forms.CharField(label="Категория", max_length=100)

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = ['name_item', 'price', 'quantity', 'info', 'restaurant', 'category', 'menu_slug']