from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from recipes_and_ingredients.models import Recipe, RecipeIngredient
from .models import CommunityRecipe
from .serializers import CommunityRecipeSerializer, AddLikeCommunitySerializer, RemoveLikesCommunitySerializer

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


class MassCommunityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        recipe = request.recipe
        communityRecipe = CommunityRecipe.objects.get(recipe=recipe)

        communityRecipeList = []
        for crec in CommunityRecipe.all():
            neededIngredients = []
            for ing in CommunityRecipe.recipe.recipe_ingredients.all():
                needed_ingredients.append(ing.ingredient.name)
            communityRecipeList.append({
                'community_recipe_id': crec.id,
                'community_recipe_name': crec.recipe.name,
                'likes': crec.likes,
                'community_recipe_ingredients': needed_ingredients,
                'photo_url': crec.photo.url,
            })

        return JsonResponse({'community_recipes': communityRecipeList})

class AddLikesCommunityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        serializer = EditSerializer(customer, data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)
        #lmao
        recipe = request.recipe
        communityRecipe = CommunityRecipe.objects.get(recipe=recipe)
        serializer = AddLikeCommunitySerializer(communityRecipe, data=request.data)
        if serializer.is_valid():
            communityRecipe = serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)

class RemoveLikesCommunityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        serializer = EditSerializer(customer, data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)
        #lmao
        recipe = request.recipe
        communityRecipe = CommunityRecipe.objects.get(recipe=recipe)
        serializer = RemoveLikesCommunitySerializer(communityRecipe, data=request.data)
        if serializer.is_valid():
            communityRecipe = serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)
