from django import forms
from delivery.models import *
from django.contrib.auth.models import User

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


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name_category', 'img_category', 'category_slug', 'restaurant_id']

    widgets = {
        'img_category': forms.FileInput(),
    }

class ItemImgForm(forms.ModelForm):
    class Meta:
        model = ImgItems
        fields = ['img_item', 'menu_item_id']


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateAdminForm(forms.ModelForm):

    class Meta:
        model = Orders
        fields = ['first_name','last_name','phone','address','total_price','order_date','status','basket']

    def __init__(self, *args, **kwargs):
        super(UpdateAdminForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            if field_name != 'status':
                self.fields[field_name].widget.attrs['readonly'] = True