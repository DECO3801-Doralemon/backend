from django.db import models
from profile_feature.models import Customer
from recipes_and_ingredients.models import Ingredient

class StoredIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    freezer_weight = models.FloatField()
    fridge_weight = models.FloatField()
    pantry_weight = models.FloatField()
