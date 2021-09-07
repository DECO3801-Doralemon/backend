from rest_framework import serializers
from recipes_and_ingredients.models import Ingredient
from profile_feature.models import Customer


class NewIngredientSerializer(serializers.Serializer):
    gtin = models.IntegerField(read_only=True)
    name = models.CharField(max_length=100)

    def create(self, validated_data):
        ingredient = Ingredient.objects.create(**validated_data)
        customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
        ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
        expiry_date = models.DateField()
        freezer_weight = models.FloatField(default=0)
        fridge_weight = models.FloatField(default=0)
        pantry_weight = models.FloatField(default=0)
        return Customer.objects.create(user=user)
