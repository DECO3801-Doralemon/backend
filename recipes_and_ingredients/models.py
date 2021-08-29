from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from profile_feature.models import Customer

# Create your models here.

class Tags(models.Model):
    tagName = models.CharField(max_length=15)
class Ingredient(models.Model):
    ingredientGTIN =  models.IntegerField(primary_key=True)
    ingredientName = models.CharField(max_length=100)
    ingredientExpiryDate = models.DateField()
    ingredientType = models.CharField(choices=[('1','Meat, Seafood & Deli'),('2','Fruit & Veg'), ('3','Dairy, Eggs & Fridge'), ('4','Bakery'), ('5','Freezer'),('6','Pantry')],
    default = 'Meat, Seafood & Deli',max_length=50)
    ingredientWeight = models.FloatField()
# freezerWeight
# pantryWeight
# fridgeWeight
class Recipe(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)
    Ingredients = models.ManyToManyField(Ingredient)

def tags_changed(sender, **kwargs):
    if kwargs['instance'].tags.count() > 3:
        raise ValidationError("You can't assign more than three tags")
m2m_changed.connect(tags_changed, sender=Recipe.tags.through)
