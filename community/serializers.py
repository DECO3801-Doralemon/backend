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
class AddLikeCommunitySerializer(serializers.Serializer):
    communityRecipe_id = serializers.IntegerField()

    def update(self, instance, validated_data):
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
