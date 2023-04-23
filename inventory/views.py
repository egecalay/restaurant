from django.shortcuts import render
# from django.http import HttpResponse # not used
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models import Sum

from .models import Ingredient, MenuItem, Purchase
from .forms import IngredientCreateForm, MenuItemCreateForm , PurchaseCreateForm ,IngredientUpdateForm

# Create your views here.

def home(request):
    context = {"name": request.user}
    return render(request,'inventory/home.html',context)


# CRUD- read
class IngredientList(ListView):
    model = Ingredient

class MenuList(ListView):
    model = MenuItem

class PurchaseList(ListView):
    model = Purchase    
    def get_revenue(self):
        revenue = Purchase.objects.aggregate(revenue=Sum("menu_item__price"))["revenue"]
        return revenue


# CRUD- create
class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = 'inventory/ingredient_add.html' 
    success_url = 'list'

class MenuItemCreate(CreateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    template_name = 'inventory/menuitem_add.html' 
    success_url = '/inventory/menu/list'

class PurchaseCreate(CreateView):
    model = Purchase
    form_class = PurchaseCreateForm
    template_name = 'inventory/purchase_add.html' 
    success_url = '/inventory/purchase/list'

# CRUD- update
class IngredientUpdate(UpdateView):
    model = Ingredient
    form_class = IngredientUpdateForm
    template_name = 'inventory/ingredient_update.html'

# CRUD- delete
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete.html'
    success_url = '/inventory/ingredient/list'
    