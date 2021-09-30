from rest_framework import serializers
from profile_feature.models import Customer
from .models import Recipe


class TagSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('author', 'name', 'tags', 'recipe_ingredients', 'customers_who_save')

class TagSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('author', 'name', 'tags', 'recipe_ingredients', 'customers_who_save')

class RISerializer(serializers.ModelSerializer):
    recipe_ingredients = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('author', 'name', 'tags', 'recipe_ingredients', 'customers_who_save')

class CWSSerializer(serializers.ModelSerializer):
    customers_who_save = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('author', 'name', 'tags', 'recipe_ingredients', 'customers_who_save')

class RecipeSerializer(serializers.Serializer):
    author = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    recipe_ingredients = models.ManyToManyField(RecipeIngredient)
    photo = serializers.ImageField(default='profilePic/GDR.PNG')
    steps = serializers.CharField(max_length=1000)
    customers_who_save = models.ManyToManyField(Customer, related_name='customers_who_saved')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return Customer.objects.create(user=user)
