from django.http.response import HttpResponse, JsonResponse
from recipes_and_ingredients.models import Ingredient
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from profile_feature.models import Customer
from recipes_and_ingredients.models import Ingredient
from .models import StoredIngredient
from .serializers import EditStoredIngredientSerializer, NewStoredIngredientSerializer
from .data_matrix_decoder import DataMatrixDecoder
from django.core.exceptions import ObjectDoesNotExist


class StorageView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        try:
            ingredient = Ingredient.objects.get(gtin=request.data['gtin'])
        except ObjectDoesNotExist:
            return JsonResponse({"gtin": "Invalid GTIN"}, status=400)

        try:
            stored_ingredient = StoredIngredient.objects.get(
                customer=customer, ingredient=ingredient)
        except ObjectDoesNotExist:
            return JsonResponse({"stored_ingredient": "Stored Ingredient not found."}, status=400)

        serializer = EditStoredIngredientSerializer(
            stored_ingredient, request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)

        return JsonResponse(serializer.errors, status=400)

    def post(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)

        data_matrix_decoder = DataMatrixDecoder()

        serializer = NewStoredIngredientSerializer(request.data_matrix)
        results = data_matrix_decoder.decode(serializer.data_matrix)
        gtin = results['01']
        expiry_date = results['15']
        ingredient = Ingredient.objects.get(gtin=gtin)
        # freezer_weight =
        # fridge_weight =
        # pantry_weight =

        return StoredIngredient.objects.create(customer=customer, ingredient=ingredient)
