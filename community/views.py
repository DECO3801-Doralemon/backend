from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import CommunityRecipe
from .serializers import CommunityRecipeSerializer


class CommunityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, community_recipe_id, format=None):
        try:
            community_recipe = CommunityRecipe.objects.get(id=community_recipe_id)
        except:
            return JsonResponse({"error": "Invalid ID value"}, status=400)

        needed_ingredients = []
        for ing in community_recipe.recipe.recipe_ingredients.all():
            needed_ingredients.append(ing.ingredient.name)

        return JsonResponse({
            'name': community_recipe.recipe.author.user.first_name + community_recipe.recipe.author.user.last_name,
            'recipe_name': community_recipe.recipe.name,
            'ingredient': needed_ingredients,
            'photo_url': community_recipe.recipe.photo.url,
            'date_time_created': community_recipe.date_time_created.strftime('%B %d %Y'),
            'steps': community_recipe.recipe.steps,
        })

    def post(self, request, format=None):
        serializer = CommunityRecipeSerializer(
            data={'recipe_id': request.POST.get('recipe_id')})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status": "OK"}, status=200)

        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, format=None):
        try:
            community_recipe_id = int(request.POST.get('community_recipe_id'))
            CommunityRecipe.objects.get(id=community_recipe_id).delete()

            return JsonResponse({"status": "OK"}, status=200)
        except ValueError:
            return JsonResponse({'error': "Invalid ID value"}, status=400)


class MassCommunityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        community_recipes = []
        for crec in CommunityRecipe.objects.all().order_by('-date_time_created'):
            needed_ingredients = []
            for ing in crec.recipe.recipe_ingredients.all():
                needed_ingredients.append(ing.ingredient.name)

            community_recipes.append({
                'id': crec.id,
                'name': crec.recipe.name,
                'needed_ingredients': needed_ingredients,
                'photo_url': crec.recipe.photo.url,
            })

        return JsonResponse({'community_recipes': community_recipes})
