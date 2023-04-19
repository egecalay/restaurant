from django.db import models

# Create your models here.
class Ingredient(models.Model):
    AvailableQty    =models.IntegerField()
    Ingredient      =models.TextField()
    Unit            =models.TextField()
    PricePerUnit    =models.DecimalField(decimal_places=2,max_digits=10)