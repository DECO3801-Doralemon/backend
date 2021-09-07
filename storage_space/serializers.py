from rest_framework import serializers
from recipes_and_ingredients.models import Ingredient
from profile_feature.models import Customer
from dataMatrixDecoder import DataMatrixDecoder
from storage_space.models import StoredIngredient


class NewStoredIngredientSerializer(serializers.Serializer):
    dataMatrix = models.CharField(max_length=100)
    weight = serializers.IntegerField()
    stored_in = serializers.ChoiceField( #implement using this like the data matrix in views, try to use the below code for help
        choices=("pantry", "freezer", "fridge"))


class StoredIngredientSerializer(serializers.Serializer):
    expired_date = serializers.DateField()
    weight = serializers.IntegerField()
    stored_in = serializers.ChoiceField(
        choices=("pantry", "freezer", "fridge"))

    def update(self, instance, validated_data):
        instance.expired_date = validated_data.get(
            'expired_date', instance.expired_date)

        if validated_data.stored_in == "pantry":
            instance.pantry_weight = validated_data.weight
        elif validated_data.stored_in == "freezer":
            instance.freezer_weight = validated_data.weight
        elif validated_data.stored_in == "fridge":
            instance.fridge_weight = validated_data.weight

        instance.save()
        return instance
