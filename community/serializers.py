from rest_framework import serializers
from recipes_and_ingredients.models import Recipe
from profile_feature.models import Customer
from .models import CommunityRecipe


class CommunityRecipeSerializer(serializers.Serializer):
    recipe_id = serializers.IntegerField()

    def create(self, validated_data):
        recipe = Recipe.objects.get(id=validated_data['recipe_id'])
        return CommunityRecipe.objects.create(recipe=recipe)
