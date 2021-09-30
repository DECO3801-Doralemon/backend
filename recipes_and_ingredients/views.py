from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from profile_feature.models import Customer
from .models import Recipe
from .serializers import MealPlannerSerializer

# Create your views here.
class AllRecipeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        recipes = []
        for recipe in Recipe.objects.all().order_by('-date_time_created'):
            needed_ingredients = []
            for ing in recipe.recipe.recipe_ingredients.all():
                needed_ingredients.append(ing.ingredient.name)

            recipes.append({
                'id': crec.id,
                'name': crec.recipe.name,
                'needed_ingredients': needed_ingredients,
                'photo_url': crec.recipe.photo.url,
            })

        return JsonResponse({'recipes': recipes})

class SingleRecipeView(APIView):
    def get(self, request, recipe_id, format=None):
        recipe = Recipe.objects.get(id=community_recipe_id)

        needed_ingredients = []
        for ing in community_recipe.recipe.recipe_ingredients.all():
            needed_ingredients.append(ing.ingredient.name)

        return JsonResponse({
            'name': community_recipe.recipe.author.user.first_name + community_recipe.recipe.author.user.last_name,
            'recipe_name': community_recipe.recipe.name,
            'ingredient': needed_ingredients,
            'photo_url': community_recipe.recipe.photo.url,
            'date_time_created': community_recipe.date_time_created.strftime('%B %d %Y')
        })
    def post(self, request, format=None):
        serializer = RecipeSerializer(
            data={'recipe_id': request.recipe_id})
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)

        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, format=None):
        try:
            recipe_id = int(request.POST.get('community_recipe_id'))
            Recipe.objects.get(id=recipe_id).delete()

            return HttpResponse(status=200)
        except ValueError:
            return JsonResponse({'error': "Invalid ID value"}, status=400)
