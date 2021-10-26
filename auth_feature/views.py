from django.shortcuts import render
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework.views import APIView

from .serializers import RegisterSerializer


class RegisterView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return JsonResponse(data={"error": "UsernameDuplicateError"}, status=400)

            return JsonResponse({"status": "Created"}, status=201)

        return JsonResponse(serializer.errors, status=400)
