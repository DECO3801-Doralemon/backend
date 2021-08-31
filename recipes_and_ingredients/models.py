from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from profile_feature.models import Customer

# Create your models here.


class Tag(models.Model):
    tagName = models.CharField(max_length=15)


class Ingredient(models.Model):
    ingredientGTIN = models.IntegerField(primary_key=True)
    ingredientName = models.CharField(max_length=100)
    ingredientType = models.CharField(choices=[('1', 'Meat, Seafood & Deli'), ('2', 'Fruit & Veg'), ('3', 'Dairy, Eggs & Fridge'), ('4', 'Bakery'), ('5', 'Freezer'), ('6', 'Pantry')],
                                      default='Meat, Seafood & Deli', max_length=50)
# freezerWeight
# pantryWeight
# fridgeWeight

    def __str__(self) -> str:
        return f"{self.ingredientGTIN} {self.ingredientName}"


class RecipeIngredient(models.Model):
    ingredientGTIN = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    weightUsedInRecipe = models.FloatField()


class Recipe(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    recipe_ingredients = models.ManyToManyField(RecipeIngredient)

    def __str__(self) -> str:
        return f"{self.author.user.username}, {self.name}"


def tags_changed(sender, **kwargs):
    if kwargs['instance'].tags.count() > 3:
        raise ValidationError("You can't assign more than three tags")


m2m_changed.connect(tags_changed, sender=Recipe.tags.through)
