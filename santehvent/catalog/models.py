from django.db import models


Garanty = (
    ('1 Year', '1 Year'),
    ('2 Year', '2 Year'),
    ('3 Year', '3 Year'),
    ('4 Year', '4 Year'),
    ('5 Year', '5 Year'),
    ('without', 'without garanty'),
)

class GroupGoods(models.Model):
    groupName = models.CharField(max_length=100)

    def __str__(self):
        """
        :return:
        """
        return self.groupName



class Manufacturer(models.Model):  # of good
    VendorName = models.CharField(max_length=100)

    def __str__(self):
        """
        :return:
        """
        return self.VendorName


class Country(models.Model):  # country of good
    CountryName = models.CharField(max_length=100)

    def __str__(self):
        """
        :return:
        """
        return self.CountryName + ' & C'


class Goods(models.Model):  # main catalog
    goodName = models.CharField(max_length=100, default='FAC1212')
    goodSquare = models.CharField(max_length=100, default='30 sq m')
    goodSizeIn = models.CharField(max_length=100, blank=True)
    goodSizeOut = models.CharField(max_length=100, blank=True)
    goodWatt = models.CharField(max_length=100, default='200W')
    goodKG = models.CharField(max_length=100, default='10 kg')
    goodGaranty = models.CharField(max_length=30, choices=Garanty, null=False, blank=False)
    goodHladagent = models.CharField(max_length=100, default='R 410A')
    goodPhoto = models.CharField(max_length=100, default='None')

    goodVendor = models.ForeignKey('Manufacturer', on_delete=models.DO_NOTHING)
    goodGroup = models.ForeignKey('GroupGoods', on_delete=models.DO_NOTHING)
    goodCountry = models.ForeignKey('Country', on_delete=models.DO_NOTHING)

    def __str__(self):
        """
        :return:
        """
        return self.goodName + ' (' + self.goodVendor.VendorName + ', ' + self.goodCountry.CountryName + ', '+ self.goodSquare + ', '+ self.goodWatt +')'


class InShop(models.Model):  # count of goods in storage
    goodID = models.CharField(max_length=100, blank=True)
    goodPrice = models.FloatField(default=0.0)
    goodcount = models.FloatField(default=0.0)
    goodreserv = models.FloatField(default=0.0)

    def __str__(self):
        return ' id =  ' + self.goodID + '; in stock ' + str(self.goodcount) + '; reserv by client ' + str(self.goodreserv) + '; our price '+ str(self.goodPrice)


class Invoice(models.Model):  # incoming goods
    goodID = models.IntegerField
    goodcount = models.IntegerField
    goodPrice = models.FloatField(default=0.0)


class Bill(models.Model):  # outcoming goods
    goodPrice = models.FloatField(default=0.0)
    goodID = models.CharField(max_length=100)
    goodcount = models.FloatField(default=0.0)
    ClientID = models.CharField(max_length=100)
