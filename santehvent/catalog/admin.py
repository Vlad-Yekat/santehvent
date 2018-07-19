from django.contrib import admin

# Register your models here.

from .models import Goods, GroupGoods, Manufacturer, Country, InShop, Invoice, Bill

admin.site.register(Goods)
admin.site.register(GroupGoods)
admin.site.register(Manufacturer)
admin.site.register(Country)
admin.site.register(InShop)
admin.site.register(Invoice)
admin.site.register(Bill)