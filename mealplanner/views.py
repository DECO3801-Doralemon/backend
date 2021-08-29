from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from profile_feature.models import Customer
from .models import MealPlan
from .serializers import MealPlannerSerializer


class MealPlanner(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, year, month, day, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)

        date = f"{year}-{month}-{day}"

        meal_plans = MealPlan.objects.filter(customer=customer, date=date)

        meal_plans_list = []
        for meal_plan in meal_plans:
            needed_ingredients = []
            for ing in meal_plan.recipe.needed_ingredients.all():
                needed_ingredients.append(str(ing))

            meal_plans_list.append({
                'ingredients': needed_ingredients,
            })

        return JsonResponse({'meal_plans': meal_plans_list})

    def post(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)

        serializer = MealPlannerSerializer(customer, data=request.data)
        if serializer.is_valid():
            meal_plan = serializer.save()
            return HttpResponse(status=200)

        return JsonResponse(serializer.errors, status=400)
