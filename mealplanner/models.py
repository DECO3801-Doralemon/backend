from django.db import models
from django.db.models.deletion import CASCADE
from profile_feature.models import Customer
from recipes_and_ingredients.models import Recipe


class MealPlan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.customer.user.username}, {self.recipe.name}, {self.date}"
