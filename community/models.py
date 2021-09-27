from django.db import models
import datetime
from recipes_and_ingredients.models import Recipe


class CommunityRecipe(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.recipe.name}"
