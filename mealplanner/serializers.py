import re
from rest_framework import serializers
from recipes_and_ingredients.models import Recipe
from .models import MealPlan


class MealPlannerSerializer(serializers.Serializer):
    recipe_id = serializers.IntegerField()
    date = serializers.DateField()

    def create(self, instance, validated_data):
        recipe = Recipe.objects.get(id=validated_data.recipe_id)

        meal_plan = MealPlan.objects.create(
            customer=instance, date=validated_data.date, recipe=recipe)
        return meal_plan
