from rest_framework import serializers
from django.contrib.auth.models import User
from profile_feature.models import Customer
from django.core.exceptions import ValidationError


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
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True, max_length=100)
    new_password = serializers.CharField(required=True, max_length=100)
