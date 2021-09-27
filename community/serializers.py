from rest_framework import serializers
from recipes_and_ingredients.models import Recipe
from profile_feature.models import Customer
from .models import CommunityRecipe


class CommunityRecipeSerializer(serializers.Serializer):
    recipe_id = serializers.IntegerField()

    def create(self, validated_data):
        recipe = Recipe.objects.get(id=validated_data['recipe_id'])
        return CommunityRecipe.objects.create(recipe=recipe)


class AddLikeCommunitySerializer(serializers.Serializer):
    community_recipe_id = serializers.IntegerField()

    def update(self, validated_data):
        instance.likes = validated_data.get('likes', instance.likes) + 1
        instance.save()
        return instance


class RemoveLikeCommunitySerializer(serializers.Serializer):
    communityRecipe_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        likesAmt = validated_data.get('likes', instance.likes)
        if likesAmt-1 <= 0:
            likesAmt = 0
        else:
            likesAmt = likesAmt - 1
        instance.likes = likesAmt
        instance.save()
        return instance
