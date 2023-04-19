from django.db import models

# Create your models here.
class Ingredient(models.Model):
    quantity    =models.IntegerField()
    name        =models.TextField()
    unit        =models.CharField(max_length=10)
    unit_price  =models.DecimalField(decimal_places=2,max_digits=10)