from django.db import models

# Create your models here.
class profile(models.Model):
    bio = models.CharField(max_length=40, Default = "");
    #can be merged later
class wasteStats(models.Model):
    totalFood =  models.IntegerField(Default = 0)
    wastedFood = models.IntegerField(Default = 0)
    foodEfficiency = models.IntegerField(Default = 0)
