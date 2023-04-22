from django.shortcuts import render
# from django.http import HttpResponse # not used
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Ingredient, MenuItem, Purchase
from .forms import IngredientCreateForm, IngredientUpdateForm

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
    
# CRUD- create
class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = 'inventory/ingredient_add.html' 

# CRUD- update
class IngredientUpdate(UpdateView):
    model = Ingredient
    form_class = IngredientUpdateForm
    template_name = 'inventory/ingredient_update.html'

# CRUD- delete
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete.html'
    