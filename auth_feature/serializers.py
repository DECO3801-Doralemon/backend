from rest_framework import serializers
from django.contrib.auth.models import User
from profile_feature.models import Customer


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return Customer.objects.create(user=user)
