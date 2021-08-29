from django.db import models
from profile_feature.models import Customer
from recipes_and_ingredients.models import Ingredient

class StoredIngredient(models.Model):
    ingredientGTIN = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredientExpiryDate = models.DateField()
    FreezerWeight = models.FloatField()
    FridgeWeight = models.FloatField()
    PantryWeight = models.FloatField()
