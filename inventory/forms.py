from django import forms
from .models import Ingredient, MenuItem, Purchase

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model   = Ingredient
        fields  = ('quantity','name','unit','unit_price')

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model   = MenuItem
        fields  = ('title','price')

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model   = Purchase
        fields  = ('day', 'time', 'menu_item', 'quantity')

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model   = Ingredient
        fields  = ('quantity','name','unit','unit_price')

