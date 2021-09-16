from rest_framework import serializers
import datetime


class CommunityRecipeSerializer(serializers.Serializer):
    recipe_id = serializers.IntegerField()
    photo = serializers.ImageField(default='profilePic/GDR.PNG')

    def create(self, validated_data):
        recipe = Recipe.objects.get(id=validated_data['recipe_id'])
        customer = Customer.objects.get(id=validated_data['customer_id'])
        communityRecipe = CommunityRecipe.objects.create(
            recipe=recipe, photo=photo)

        return communityRecipe
