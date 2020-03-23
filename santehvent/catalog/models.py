from django.db import models
from django.conf import settings


GARANTY = (
    ("1 Year", "1 Year"),
    ("2 Year", "2 Year"),
    ("3 Year", "3 Year"),
    ("4 Year", "4 Year"),
    ("5 Year", "5 Year"),
    ("without", "without garanty"),
)


class GroupGoods(models.Model):
    group_name = models.CharField(max_length=100)

    def __str__(self):
        """
        :return:
        """
        return self.group_name


class Manufacturer(models.Model):  # of good
    vendor_name = models.CharField(max_length=100)

    def __str__(self):
        """
        :return:
        """
        return self.vendor_name


class Country(models.Model):  # country of good
    country_name = models.CharField(max_length=100)

    def __str__(self):
        """
        :return:
        """
        return self.country_name + " & C"


class Goods(models.Model):  # main catalog
    good_name = models.CharField(max_length=100, default="FAC1212")
    good_square = models.CharField(max_length=100, default="30 sq m")
    good_size_in = models.CharField(max_length=100, blank=True)
    good_size_out = models.CharField(max_length=100, blank=True)
    good_watt = models.CharField(max_length=100, default="200W")
    good_kg = models.CharField(max_length=100, default="10 kg")
    good_garanty = models.CharField(
        max_length=30, choices=GARANTY, null=False, blank=False
    )
    good_hladagent = models.CharField(max_length=100, default="R 410A")
    good_photo = models.CharField(max_length=100, default="None")

    good_vendor = models.ForeignKey("Manufacturer", on_delete=models.DO_NOTHING)
    good_group = models.ForeignKey("GroupGoods", on_delete=models.DO_NOTHING)
    good_country = models.ForeignKey("Country", on_delete=models.DO_NOTHING)

    def __str__(self):
        """
        :return:
        """
        return (
            self.good_name
            + " ("
            + self.good_vendor.vendor_name
            + ", "
            + self.good_country.country_name
            + ", "
            + self.good_square
            + ", "
            + self.good_watt
            + ")"
        )


class InShop(models.Model):  # count of goods in storage
    good_id = models.CharField(max_length=100, blank=True)
    good_price = models.FloatField(default=0.0)
    good_count = models.FloatField(default=0.0)
    good_reserv = models.FloatField(default=0.0)

    def __str__(self):
        return (
            " id =  "
            + self.good_id
            + "; in stock "
            + str(self.good_count)
            + "; reserved by client "
            + str(self.good_reserv)
            + "; our price "
            + str(self.good_price)
        )


class Invoice(models.Model):  # incoming goods
    good_id = models.IntegerField
    good_count = models.IntegerField
    good_price = models.FloatField(default=0.0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE
    )


class Bill(models.Model):  # outcoming goods
    good_price = models.FloatField(default=0.0)
    good_id = models.CharField(max_length=100)
    good_count = models.FloatField(default=0.0)
    client_id = models.CharField(max_length=100)
    # email = models.Emailfileds()
