from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profilePic')
class AvoidedFood(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
class WasteStat(models.Model):
    totalFood =  models.IntegerField(default = 0)
    wastedFood = models.IntegerField(default = 0)
    foodEfficiency = models.IntegerField(default = 0)
