import re
from rest_framework import serializers
from recipes_and_ingredients.models import Recipe
from profile_feature.models import Customer
from .models import MealPlan


class MealPlannerSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    recipe_id = serializers.IntegerField()
    date = serializers.DateField()

    def create(self, validated_data):
        recipe = Recipe.objects.get(id=validated_data['recipe_id'])
        customer = Customer.objects.get(id=validated_data['customer_id'])

        meal_plan = MealPlan.objects.create(
            customer=customer, date=validated_data['date'], recipe=recipe)
        
        return meal_plan
