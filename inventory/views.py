from django.shortcuts import render
# from django.http import HttpResponse # not used
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Ingredient
from .forms import IngredientCreateForm, IngredientUpdateForm

# Create your views here.

def home(request):
    return render(request,'inventory/home.html')

class IngredientList(ListView):
    model = Ingredient
    

class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = 'inventory/ingredient_add.html' 

class IngredientUpdate(UpdateView):
    model = Ingredient
    form_class = IngredientUpdateForm
    template_name = 'inventory/ingredient_update.html'

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete.html'
    