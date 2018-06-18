from django.db import models

# Create your models here.
class good(models.Model):
    qoodName = models.CharField(max_length=100,default='FAC1212')
    goodGroup = models.CharField(max_length=100,default= 'Invertor')
    goodSquare = models.CharField(max_length=100,default='30 sq m')
    goodSizeIn = models.CharField(max_length=100,default='80*20*30')
    goodSizeOut = models.CharField(max_length=100,default='100*50*40')
    goodWatt = models.CharField(max_length=100,default='200W')
    goodKG = models.CharField(max_length=100, default='10 kg')
    goodCountry = models.CharField(max_length=100, default='China')
    goodGaranty = models.CharField(max_length=100, default='1 year')
    goodHladagent = models.CharField(max_length=100, default='R 410A')

class group(models.Model):
    groupName = models.CharField(max_length=100)

class inShop(models.Model):
    goodID = models.IntegerField
    goodPrice = models.FloatField(default=0.0)
    goodcount = models.IntegerField
    goodreserv = models.IntegerField


