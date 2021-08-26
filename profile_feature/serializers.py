from rest_framework import serializers
from django.contrib.auth.models import User
from profile_feature.models import Customer
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class EditSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    bio = serializers.CharField(max_length=100, allow_blank=True)
    photo = serializers.ImageField(default='profilePic/GDR.PNG')

    def update(self, instance, validated_data):
        instance.user.first_name = validated_data.get(
            'first_name', instance.user.first_name)
        instance.user.last_name = validated_data.get(
            'last_name', instance.user.last_name)
        instance.user.email = validated_data.get('email', instance.user.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance

class EditPasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        # print(validate_password(value))
        print(value)
        validate_password(value)
        return value
