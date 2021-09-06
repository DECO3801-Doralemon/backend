from django.db import models
from profile_feature.models import Customer
from recipes_and_ingredients.models import Ingredient

class StoredIngredient(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    freezer_weight = models.FloatField(default=0)
    fridge_weight = models.FloatField(default=0)
    pantry_weight = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"{self.customer}, {self.ingredient}"
