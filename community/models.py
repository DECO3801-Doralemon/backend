from django.db import models
from recipes_and_ingredients.models import Recipe

# Create your models here.
class OnlineRecipe(models.Model):
    recipe= models.ForeignKey(Recipe, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.recipe}"
