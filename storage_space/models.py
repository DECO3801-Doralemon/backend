from django.db import models
from profile_feature.models import Customer
from recipes_and_ingredients.models import Ingredient

class StoredIngredientInFreezer(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    kg = models.FloatField(default=1)

    def __str__(self) -> str:
        return f"{self.customer}, {self.ingredient}"


class StoredIngredientInFridge(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    kg = models.FloatField(default=1)

    def __str__(self) -> str:
        return f"{self.customer}, {self.ingredient}"


class StoredIngredientInPantry(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    kg = models.FloatField(default=1)

    def __str__(self) -> str:
        return f"{self.customer}, {self.ingredient}"
