from rest_framework import serializers
from profile_feature.models import Customer
from .models import Recipe
import json


class TagSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('author', 'name', 'tags', 'recipe_ingredients', 'customers_who_save')

class RISerializer(serializers.HyperlinkedModelSerializer):
    recipe_ingredients = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('author', 'name', 'tags', 'recipe_ingredients', 'customers_who_save')

class RecipeSerializer(serializers.Serializer):
    author = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    tags = serializers.CharField(max_length=100)
    recipe_ingredients = serializers.CharField(max_length=100)
    photo = serializers.ImageField(default='profilePic/GDR.PNG')
    steps = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return Customer.objects.create(user=user)
