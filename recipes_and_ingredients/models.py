from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from profile_feature.models import Customer

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=15)


class Ingredient(models.Model):
    gtin = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name} {self.type}"


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    weight_used = models.FloatField()

    def __str__(self) -> str:
        return f"{self.ingredient}, {self.weight_used}"


class Recipe(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    recipe_ingredients = models.ManyToManyField(RecipeIngredient)

    def __str__(self) -> str:
        return f"{self.author.user.username}, {self.name}"


def tags_changed(sender, **kwargs):
    if kwargs['instance'].tags.count() > 3:
        raise ValidationError("You can't assign more than three tags")


m2m_changed.connect(tags_changed, sender=Recipe.tags.through)
