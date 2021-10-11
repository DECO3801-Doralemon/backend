from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
import json
from profile_feature.models import Customer
from .models import Ingredient, Recipe, RecipeIngredient, Tag

# Create your views here.


class AllRecipeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        recipes = []
        for recipe in Recipe.objects.all().order_by('-time_created'):
            needed_ingredients = []
            for ing in recipe.recipe_ingredients.all():
                needed_ingredients.append(ing.ingredient.name)

            recipes.append({
                'id': recipe.id,
                'name': recipe.name,
                'needed_ingredients': needed_ingredients,
                'photo_url': recipe.photo.url,
            })

        return JsonResponse({'recipes': recipes})


class SingleRecipeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, recipe_id, format=None):
        recipe = Recipe.objects.get(id=recipe_id)

        needed_ingredients = []
        for ing in recipe.recipe_ingredients.all():
            needed_ingredients.append(ing.ingredient.name)

        return JsonResponse({
            'name': recipe.author.user.first_name + recipe.author.user.last_name,
            'recipe_name': recipe.name,
            'ingredient': needed_ingredients,
            'photo_url': recipe.photo.url,
            'time_created': recipe.time_created.strftime('%B %d %Y')
        })

    def post(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        name = request.data["name"]
        photo = request.data["photo"]
        steps = request.data["steps"]

        tag_ids = json.loads(request.data["tags"])
        tags = []
        for id in tag_ids:
            try:
                tags.append(Tag.objects.get(id=id))
            except ObjectDoesNotExist:
                return JsonResponse({'error': "Invalid tags ID value"}, status=400)

        recipe_ingredients_data = json.loads(
            request.data["recipe_ingredients"])
        recipe_ingredients = []
        for data in recipe_ingredients_data:
            try:
                ing = Ingredient.objects.get(id=data['id'])
            except ObjectDoesNotExist:
                return JsonResponse({'error': "Invalid Ingredient ID value"}, status=400)

            recipe_ingredients.append(RecipeIngredient.objects.create(
                ingredient=ing, kg_used=data['kg_used']))

        recipe = Recipe.objects.create(
            author=customer, name=name, photo=photo, steps=steps)
        recipe.tags.set(tags)
        recipe.recipe_ingredients.set(recipe_ingredients)
        recipe.customers_who_save.set([customer])

        return HttpResponse(status=201)

    def delete(self, request, format=None):
        try:
            recipe_id = int(request.POST.get('recipe_id'))
            Recipe.objects.get(id=recipe_id).delete()

            return HttpResponse(status=200)
        except ValueError:
            return JsonResponse({'error': "Invalid ID value"}, status=400)
