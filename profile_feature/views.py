from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Customer
from .serializers import EditSerializer, EditPasswordSerializer
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import WasteStat, Customer

response = {}


class Profile(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        return JsonResponse({
            'First Name': customer.user.first_name,
            'Last Name': customer.user.last_name,
            'Username': customer.user.username,
            'Email': customer.user.email,
            'Biography': customer.bio,
            'Photo': customer.photo.url,
        })

    def post(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        serializer = EditSerializer(customer, data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)


class EditPassword(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        serializer = EditPasswordSerializer(user, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)
