from django.http.response import HttpResponse, JsonResponse
from recipes_and_ingredients.models import Ingredient
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from profile_feature.models import Customer
from recipes_and_ingredients.models import Ingredient
from .models import StoredIngredient
from .serializers import StoredIngredientSerializer, NewStoredIngredientSerializer
from dataMatrixDecoder import DataMatrixDecoder


def StoredIngredientView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        ingredient = Ingredient.objects.get(gtin=request.gtin)

        stored_ingredient = StoredIngredient.objects.get(
            customer=customer, ingredient=ingredient)

        serializer = StoredIngredientSerializer(stored_ingredient, request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)

        return JsonResponse(serializer.errors, status=400)

    def post(self, request, format = None):
        serializer = NewStoredIngredientSerializer(request.dataMatrix)
        user = request.user
        customer = Customer.objects.get(user=user)
        dataMatrixDecoder = DataMatrixDecoder()
        results = dataMatrixDecoder.decode(serializer.validate_dataMatrix)
        gtin = results['01']
        expiry_date = results['15']
        ingredient = Ingredient.objects.get(gtin=gtin)
        freezer_weight = 0
        fridge_weight = 0
        pantry_weight = 0
        loc = serializer.validate_stored_in
        validatedWeight = serializer.validate_weight
        if loc == "pantry":
            pantry_weight = validatedWeight
        elif loc == "freezer":
            freezer_weight = validatedWeight
        elif loc == "fridge":
            fridge_weight = validatedWeight
        return StoredIngredient.objects.create(customer=customer, ingredient = ingredient, pantry_weight = pantry_weight, freezer_weight = freezer_weight, fridge_weight = fridge_weight)
