from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from profile_feature.models import Customer
from .models import Recipe

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
                'id': recipe.id,
                'name': recipe.recipe.name,
                'needed_ingredients': needed_ingredients,
                'photo_url': recipe.recipe.photo.url,
            })

        return JsonResponse({'recipes': recipes})

class SingleRecipeView(APIView):
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
            'date_time_created': recipe.date_time_created.strftime('%B %d %Y')
        })
    def post(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        name = request.data["name"]
        tags = json.loads(request.data["tags"])
        recipe_ingredients = json.loads(request.data["recipe_ingredients"])
        photo = request.data["photo"]
        steps = request.data["steps"]
        customers_who_save = request.data["customers_who_save"]
        Recipe.objects.create(author=customer, name=name, tags = tags, recipe_ingredients = recipe_ingredients, photo = photo, steps = steps, customers_who_save = customers_who_save)
        return HttpResponse(status=201)

    def delete(self, request, format=None):
        try:
            recipe_id = int(request.POST.get('recipe_id'))
            Recipe.objects.get(id=recipe_id).delete()

            return HttpResponse(status=200)
        except ValueError:
            return JsonResponse({'error': "Invalid ID value"}, status=400)
