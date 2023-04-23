from django.db import models


# Create your models here.
class Ingredient(models.Model):
    quantity    =models.IntegerField()
    name        =models.TextField()
    unit        =models.CharField(max_length=10)
    unit_price  =models.DecimalField(decimal_places=2,max_digits=4)

class MenuItem(models.Model):
    title       = models.TextField()
    price       = models.DecimalField(decimal_places=2,max_digits=4)
    # TODO - add menu sections

class RecipeRequirement(models.Model):
    ingredient  = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    menu_item   = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity    = models.DecimalField(decimal_places=2,max_digits=4)
    # TODO- add units as foreign key from Ingredients table
    # add feeds or servings or yield fields

class Purchase(models.Model):
    day         = models.DateField(auto_now=False, auto_now_add=False)
    time        = models.TimeField(auto_now=False, auto_now_add=False)
    menu_item   = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity    = models.DecimalField(decimal_places=2,max_digits=4)

    def sub_total(self):
        sub_total = self.menu_item.price * self.quantity
        return round(sub_total,2)
    

    #TODO- add date/time of the order
    #TODO- add User for the waiter/waitress with authentication
    #TODO- add table number for the order
    