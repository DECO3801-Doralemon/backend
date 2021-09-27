from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from profile_feature.models import Customer

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    gtin = models.CharField(unique=True, max_length=14)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='ingredients', default='ingredients/test_photo.PNG')

    def __str__(self) -> str:
        return f"{self.gtin} {self.name}"


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    kg_used = models.FloatField()

    def __str__(self) -> str:
        return f"{self.ingredient}, {self.kg_used}"


class Recipe(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='author')
    time_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    recipe_ingredients = models.ManyToManyField(RecipeIngredient)
    photo = models.ImageField(upload_to='recipes', default='recipes/test_photo.PNG')
    steps = models.TextField(max_length=1000)
    customers_who_save = models.ManyToManyField(Customer, related_name='customers_who_saved')

    def __str__(self) -> str:
        return f"{self.author.user.username}, {self.name}"


def tags_changed(sender, **kwargs):
    if kwargs['instance'].tags.count() > 3:
        raise ValidationError("You can't assign more than three tags")


m2m_changed.connect(tags_changed, sender=Recipe.tags.through)
