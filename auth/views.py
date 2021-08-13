from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from .serializers import RegisterSerializer


class RegisterView(APIView):

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            response = JsonResponse(status=201)

            # Add cookie to user to be automatically
            # authenticated in different pages
            response.set_cookie('auth_token', Token.objects.create(user=user))

            return response

        return JsonResponse(serializer.errors, status=400)
