from django.http.response import HttpResponse, JsonResponse
from recipes_and_ingredients.models import Ingredient
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import date
from profile_feature.models import Customer
from recipes_and_ingredients.models import Ingredient
from .models import StoredIngredientInFreezer, StoredIngredientInFridge, StoredIngredientInPantry
from .serializers import EditStorageSerializer
from .data_matrix_decoder import DataMatrixDecoder


class StorageView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def decode(self, request):
        user = request.user
        customer = Customer.objects.get(user=user)

        data_matrix_decoder = DataMatrixDecoder()

        results = data_matrix_decoder.decode(request.data['data_matrix'])
        gtin = results['01']
        expiry_date = results['15']
        kg = float(results['310'])

        ingredient = Ingredient.objects.get(gtin=gtin)

        return (customer, ingredient, expiry_date, kg)

    def stored_ingredient_to_json_response(self, stored_ingredients):
        response = []
        for ing in stored_ingredients:
            response.append({
                'id': ing.id,
                'gtin': ing.ingredient.gtin,
                'name': ing.ingredient.name,
                'expiry_countdown_in_days': abs(date.today() - ing.expiry_date).days,
                'kg': ing.kg,
            })

        return JsonResponse({'stored_ingredients': response})

    def save_put_data(self, stored_ingredient, data):
        serializer = EditStorageSerializer(
            stored_ingredient, data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)

        return JsonResponse(serializer.errors, status=400)


class FreezerStorageView(StorageView):

    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)

        stored_ingredients = StoredIngredientInFreezer.objects.filter(
            customer=customer)
        return self.stored_ingredient_to_json_response(stored_ingredients)

    def put(self, request, format=None):
        stored_ingredient = StoredIngredientInFreezer.objects.get(
            id=request.data['id'])

        return self.save_put_data(stored_ingredient, request.data)

    def post(self, request, format=None):
        (customer, ingredient, expiry_date, kg) = self.decode(request)
        StoredIngredientInFreezer.objects.create(customer=customer, ingredient=ingredient, expiry_date=expiry_date, kg=kg)

        return JsonResponse(status=201)

    def delete(self, request, format=None):
        StoredIngredientInFreezer.objects.get(id=request.data['id']).delete()

        return JsonResponse(status=200)


class FridgeStorageView(StorageView):
    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)

        stored_ingredients = StoredIngredientInFridge.objects.filter(
            customer=customer)
        return self.stored_ingredient_to_json_response(stored_ingredients)

    def put(self, request, format=None):
        stored_ingredient = StoredIngredientInFridge.objects.get(
            id=request.data['id'])

        return self.save_put_data(stored_ingredient, request.data)

    def post(self, request, format=None):
        (customer, ingredient, expiry_date, kg) = self.decode(request)
        StoredIngredientInFridge.objects.create(customer=customer, ingredient=ingredient, expiry_date=expiry_date, kg=kg)

        return JsonResponse(status=201)

    def delete(self, request, format=None):
        StoredIngredientInFridge.objects.get(id=request.data['id']).delete()

        return JsonResponse(status=200)


class PantryStorageView(StorageView):
    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)

        stored_ingredients = StoredIngredientInPantry.objects.filter(
            customer=customer)
        return self.stored_ingredient_to_json_response(stored_ingredients)

    def put(self, request, format=None):
        stored_ingredient = StoredIngredientInPantry.objects.get(
            id=request.data['id'])

        return self.save_put_data(stored_ingredient, request.data)

    def post(self, request, format=None):
        (customer, ingredient, expiry_date, kg) = self.decode(request)
        StoredIngredientInFridge.objects.create(customer=customer, ingredient=ingredient, expiry_date=expiry_date, kg=kg)

        return JsonResponse(status=201)

    def delete(self, request, format=None):
        StoredIngredientInPantry.objects.get(id=request.data['id']).delete()

        return JsonResponse(status=200)
