from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from profile_feature.models import Customer
from recipes_and_ingredients.models import Recipe
from .models import CommunityRecipe
from .serializers import CommunityRecipeSerializer, AddLikeCommunitySerializer, RemoveLikeCommunitySerializer


class CommunityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, community_recipe_id, format=None):
        community_recipe = CommunityRecipe.objects.get(id=community_recipe_id)

        needed_ingredients = []
        for ing in community_recipe.recipe.recipe_ingredients.all():
            needed_ingredients.append(ing.ingredient.name)

        return JsonResponse({
            'name': community_recipe.recipe.author.user.first_name + community_recipe.recipe.author.user.last_name,
            'recipe_name': community_recipe.recipe.name,
            'likes': community_recipe.likes,
            'ingredient': needed_ingredients,
            'photo_url': community_recipe.recipe.photo.url,
            'date_time_created': community_recipe.date_time_created.strftime('%B %d %Y')
        })

    def post(self, request, format=None):
        serializer = CommunityRecipeSerializer(
            data={'recipe_id': request.recipe_id})
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)

        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, format=None):
        try:
            community_recipe_id = int(request.POST.get('community_recipe_id'))
            CommunityRecipe.objects.get(id=community_recipe_id).delete()

            return HttpResponse(status=200)
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
                'likes': crec.likes,
                'needed_ingredients': needed_ingredients,
                'photo_url': crec.recipe.photo.url,
            })

        return JsonResponse({'community_recipes': community_recipes})


class AddLikesCommunityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        community_recipe_id = request.community_recipe_id
        community_recipe = CommunityRecipe.objects.get(id=community_recipe_id)
        community_recipe.likes += 1
        community_recipe.save()

        return HttpResponse(status=200)


class RemoveLikesCommunityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        community_recipe_id = request.community_recipe_id
        community_recipe = CommunityRecipe.objects.get(id=community_recipe_id)
        community_recipe.likes -= 1
        community_recipe.save()

        return HttpResponse(status=200)
