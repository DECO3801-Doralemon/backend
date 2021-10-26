from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Customer
from .serializers import EditSerializer, EditPasswordSerializer
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response

from .models import Customer


class ProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        return JsonResponse({
            'first_name': customer.user.first_name,
            'last_name': customer.user.last_name,
            'username': customer.user.username,
            'email': customer.user.email,
            'biography': customer.bio,
            'photo_url': customer.photo.url,
        })

    def post(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        serializer = EditSerializer(customer, data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)


class EditPasswordView(APIView):
    """
    An endpoint for changing password.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = EditPasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return JsonResponse({"old_password": ["Wrong password."]},
                                status=400)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return JsonResponse(status=204)

        return JsonResponse(serializer.errors, status=400)
