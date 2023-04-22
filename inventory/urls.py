from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('inventory/ingredient/list', views.IngredientList.as_view(),name='ingredientlist'),
    path('inventory/ingredient/add', views.IngredientCreate.as_view(),name='ingredientcreate'),
    path('inventory/ingredient/<pk>/change', views.IngredientUpdate.as_view(),name='ingredientupdate'),
    path('inventory/ingredient/<pk>/delete', views.IngredientDelete.as_view(),name='ingredientdelete'),
    path('inventory/menu/list', views.MenuList.as_view(),name='menulist'),
    path('inventory/purchase/list', views.PurchaseList.as_view(),name='purchaselist'),



]