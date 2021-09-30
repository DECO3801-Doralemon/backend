from django.db import models
from recipes_and_ingredients.models import Recipe


class CommunityRecipe(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.recipe.name}"
