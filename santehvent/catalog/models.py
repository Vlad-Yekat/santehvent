from django.db import models

# Create your models here.
class good(models.Model):
    qoodName = models.CharField(max_length=100)
    goodPrice = models.FloatField(default=0.0)

class group(models.Model):
    groupName = models.CharField(max_length=100)

class inShop(models.Model):
    goodID = models.IntegerField
    goodcount = models.IntegerField


