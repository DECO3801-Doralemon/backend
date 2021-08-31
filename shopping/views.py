from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from datetime import date, timedelta
from profile_feature.models import Customer
from mealplanner.models import MealPlan


class ShoppingView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        def iterate_thirty_days(start_date):
            for n in range(30):
                yield start_date + timedelta(n)

        user = request.user
        customer = Customer.objects.get(user=user)

        TODAY = date(2021, 8, 20)
        meal_plans_ingredients = []
        for single_date in iterate_thirty_days(TODAY):
            for meal_plan in MealPlan.objects.filter(
                    date=single_date, customer=customer):
                for recipe_ingredient in meal_plan.recipe.recipe_ingredients.all():
                    meal_plans_ingredients.append(
                        (recipe_ingredient.ingredient.name, recipe_ingredient.weight_used))
        
        # TODO
        return JsonResponse({'test': meal_plans_ingredients})
