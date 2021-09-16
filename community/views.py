from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from recipes_and_ingredients.models import Recipe, RecipeIngredient
from .models import CommunityRecipe
from .serializers import CommunityRecipeSerializer

# Create your views here.
class CommunityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        recipe = request.recipe
        communityRecipe = CommunityRecipe.objects.get(recipe=recipe)

        neededIngredients = []
        for ing in CommunityRecipe.recipe.recipe_ingredients.all():
            needed_ingredients.append(ing.ingredient.name)

        return JsonResponse({
            'first_name': CommunityRecipe.recipe.customer.user.first_name,
            'last_name': CommunityRecipe.recipe.customer.user.last_name,
            'recipe_name': CommunityRecipe.recipe.name,
            'likes': CommunityRecipe.likes,
            'ingredient': neededIngredients,
            'photo_url': CommunityRecipe.photo.url,
        })

    def post(self, request, format=None):
        recipe = request.recipe
        communityRecipe = CommunityRecipe.objects.get(recipe=recipe)
        serializer = CommunityRecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            communityRecipe = serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, format=None):
        try:
            CommunityRecipe_id = int(request.POST.get('CommunityRecipe_id'))
            CommunityRecipe.objects.get(id=CommunityRecipe_id).delete()

            return HttpResponse(status=200)
        except ValueError:
            return JsonResponse({'error': "Invalid ID Value"}, status=400)


class BigCommunityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        recipe = request.recipe
        communityRecipe = CommunityRecipe.objects.get(recipe=recipe)

        communityRecipeList = []
        for crec in CommunityRecipe.all():
            communityRecipeList.append(crec)

        return JsonResponse({
            'first_name': CommunityRecipe.recipe.customer.user.first_name,
            'last_name': CommunityRecipe.recipe.customer.user.last_name,
            'recipe_name': CommunityRecipe.recipe.name,
            'likes': CommunityRecipe.likes,
            'ingredient': neededIngredients,
            'photo_url': CommunityRecipe.photo.url,
        })

    def post(self, request, format=None):
        recipe = request.recipe
        communityRecipe = CommunityRecipe.objects.get(recipe=recipe)
        serializer = CommunityRecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            communityRecipe = serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, format=None):
        try:
            meal_plan_id = int(request.POST.get('meal_plan_id'))
            MealPlan.objects.get(id=meal_plan_id).delete()

            return HttpResponse(status=200)
        except ValueError:
            return JsonResponse({'error': "Invalid ID Value"}, status=400)
