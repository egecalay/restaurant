from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('inventory/ingredient/list', views.IngredientList.as_view(),name='ingredientlist'),
    path('inventory/ingredient/add', views.IngredientCreate.as_view(),name='ingredientcreate'),
    path('inventory/ingredient/<pk>/change', views.IngredientUpdate.as_view(),name='ingredientupdate'),
    path('inventory/ingredient/<pk>/delete', views.IngredientDelete.as_view(),name='ingredientdelete'),
    path('inventory/menu/list', views.MenuList.as_view(),name='menuitemlist'),
    path('inventory/menu/add', views.MenuItemCreate.as_view(),name='menuitemcreate'),
    path('inventory/purchase/add', views.PurchaseCreate.as_view(),name='purchasecreate'),
    path('inventory/purchase/list', views.PurchaseList.as_view(),name='purchaselist'),



]