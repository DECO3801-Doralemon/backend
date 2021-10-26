from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class EditSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    email = serializers.CharField(max_length=100, required=False)
    bio = serializers.CharField(max_length=100, required=False)
    photo = serializers.ImageField(required=False)

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
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
