import storage_space
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from datetime import date, timedelta
from profile_feature.models import Customer
from mealplanner.models import MealPlan
from storage_space.models import StoredIngredientInFreezer, StoredIngredientInFridge, StoredIngredientInPantry


class ShoppingView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        def iterate_thirty_days(start_date):
            for n in range(30):
                yield start_date + timedelta(n)

        def merge_ingredients(ingredients):
            i = 0
            j = 1
            size = len(ingredients)
            while i < size:
                while j < size:
                    if ingredients[i][0].id == ingredients[j][0].id:
                        ingredients[i][1] += ingredients[j][1]
                        ingredients.pop(j)
                        size = len(ingredients)
                    else:
                        j += 1
                i += 1
                j = i + 1

        user = request.user
        customer = Customer.objects.get(user=user)

        TODAY = date.today()
        ingredients = []
        for single_date in iterate_thirty_days(TODAY):
            for meal_plan in MealPlan.objects.filter(
                    date=single_date, customer=customer):
                for recipe_ingredient in meal_plan.recipe.recipe_ingredients.all():
                    ingredients.append(
                        [recipe_ingredient.ingredient, recipe_ingredient.kg_used])

        merge_ingredients(ingredients)

        needed_ingredients = []
        for (ingredient, kg_used) in ingredients:
            kg_stored_in_freezer, kg_stored_in_fridge, kg_stored_in_pantry = 0, 0, 0
            try:
                kg_stored_in_freezer = StoredIngredientInFreezer.objects.get(
                    customer=customer, ingredient=ingredient).kg
            except: None
            try:
                kg_stored_in_fridge = StoredIngredientInFridge.objects.get(
                    customer=customer, ingredient=ingredient).kg
            except: None
            try:
                kg_stored_in_pantry = StoredIngredientInPantry.objects.get(
                    customer=customer, ingredient=ingredient).kg
            except:
                None

            kg_total = kg_stored_in_freezer + kg_stored_in_fridge + kg_stored_in_pantry

            if kg_total == 0:
                needed_ingredients.append({
                    "id": ingredient.id,
                    "gtin": ingredient.gtin,
                    "name": ingredient.name,
                    "needed_kg": kg_used,
                })
            else:
                needed_kg = kg_used - kg_total

                if needed_kg > 0:
                    needed_ingredients.append({
                        "id": ingredient.id,
                        "gtin": ingredient.gtin,
                        "name": ingredient.name,
                        "needed_kg": needed_kg,
                    })

        return JsonResponse({'needed_ingredients': needed_ingredients})
