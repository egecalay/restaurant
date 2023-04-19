from django import forms
from .models import Ingredient

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model   = Ingredient
        fields  = ('quantity','name','unit','unit_price')

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model   = Ingredient
        fields  = ('quantity','name','unit','unit_price')

