from django.http.response import HttpResponse, JsonResponse
from recipes_and_ingredients.models import Ingredient
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import date
from profile_feature.models import Customer
from recipes_and_ingredients.models import Ingredient
from .models import StoredIngredientInFreezer, StoredIngredientInFridge, StoredIngredientInPantry
from .serializers import CreateStorageSerializer, EditFreezerStorageSerializer, EditFridgeStorageSerializer, EditPantryStorageSerializer
from .data_matrix_decoder import DataMatrixDecoder


class StorageView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def decode(self, request):
        user = request.user
        customer = Customer.objects.get(user=user)

        data_matrix_decoder = DataMatrixDecoder()

        serializer = CreateStorageSerializer(request.data_matrix)
        results = data_matrix_decoder.decode(serializer.data_matrix)
        gtin = results['01']
        expiry_date = results['15']
        kg = results['310']

        ingredient = Ingredient.objects.get(gtin=gtin)

        return (customer, ingredient, expiry_date, kg)

    def stored_ingredient_to_json_response(self, stored_ingredients):
        response = []
        for ing in stored_ingredients:
            response.append({
                'gtin': ing.ingredient.gtin,
                'name': ing.ingredient.name,
                'expiry_countdown': abs(date.today() - ing.expiry_date).days,
                'kg': ing.kg,
            })

        return JsonResponse({'stored_ingredients': response})


class FreezerStorageView(StorageView):

    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)

        stored_ingredients = StoredIngredientInFreezer.objects.filter(
            customer=customer)
        return self.stored_ingredient_to_json_response(stored_ingredients)

    def put(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        ingredient = Ingredient.objects.get(gtin=request.data['gtin'])

        stored_ingredient = StoredIngredientInFreezer.objects.get(
            customer=customer, ingredient=ingredient)

        serializer = EditFreezerStorageSerializer(
            stored_ingredient, request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)

        return JsonResponse(serializer.errors, status=400)

    def post(self, request, format=None):
        (customer, ingredient, expiry_date, kg) = self.decode(request)
        return StoredIngredientInFreezer.objects.create(customer=customer, ingredient=ingredient, expiry_date=expiry_date, kg=kg)


class FridgeStorageView(StorageView):
    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)

        stored_ingredients = StoredIngredientInFreezer.objects.filter(
            customer=customer)
        return self.stored_ingredient_to_json_response(stored_ingredients)

    def put(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        ingredient = Ingredient.objects.get(gtin=request.data['gtin'])

        stored_ingredient = StoredIngredientInFridge.objects.get(
            customer=customer, ingredient=ingredient)

        serializer = EditFridgeStorageSerializer(
            stored_ingredient, request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)

        return JsonResponse(serializer.errors, status=400)

    def post(self, request, format=None):
        (customer, ingredient, expiry_date, kg) = self.decode(request)
        return StoredIngredientInFridge.objects.create(customer=customer, ingredient=ingredient, expiry_date=expiry_date, kg=kg)


class PantryStorageView(StorageView):
    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)

        stored_ingredients = StoredIngredientInFreezer.objects.filter(
            customer=customer)
        return self.stored_ingredient_to_json_response(stored_ingredients)

    def put(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        ingredient = Ingredient.objects.get(gtin=request.data['gtin'])

        stored_ingredient = StoredIngredientInPantry.objects.get(
            customer=customer, ingredient=ingredient)

        serializer = EditPantryStorageSerializer(
            stored_ingredient, request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)

        return JsonResponse(serializer.errors, status=400)

    def post(self, request, format=None):
        (customer, ingredient, expiry_date, kg) = self.decode(request)
        return StoredIngredientInFridge.objects.create(customer=customer, ingredient=ingredient, expiry_date=expiry_date, kg=kg)
