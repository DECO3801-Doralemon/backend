from rest_framework.views import APIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Customer
from .serializers import EditSerializer, EditPasswordSerializer
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

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



class EditPassword(UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = EditPasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
