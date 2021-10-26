from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100, blank=True, null=True)
    photo = models.ImageField(
        upload_to='profile_photos', default='profile_photos/test_photo.png', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"


class WasteStat(models.Model):
    totalFood = models.IntegerField(default=0)
    wastedFood = models.IntegerField(default=0)
    foodEfficiency = models.IntegerField(default=0)
