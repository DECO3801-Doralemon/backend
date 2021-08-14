from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse

from .models import AvoidedFood, WasteStat, Customer

response={}

class Profile(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user = user)
        dict = {
        'Username': customer.user.username,
        'Biography': customer.bio,
        'Photo': customer.photo.url,
        }
        return JsonResponse(dict)
    def post(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
