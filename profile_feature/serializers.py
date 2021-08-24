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
    oldPassword = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def update(self, instance, validated_data):
        if user.check_password(validated_data.oldPassword):
            if user.check_password(validated_data.password):
                raise ValidationError("Password is the same as old password.")
            else:
                instance.set_password(validated_data.password)
                instance.save()
                return instance
        else:
            raise ValidationError("Wrong password.")
