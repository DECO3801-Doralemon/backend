from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import AvoidedFood, WasteStat, Customer
from django.http import JsonResponse

response={}

class Profile(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user = user)
        dict = {
        'Username': customer.user.username,
        'Biography': customer.bio,
        'Photo': customer.photo
        }
        return JsonResponse(dict)
    def post(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
