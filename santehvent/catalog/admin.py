from django.contrib import admin

# Register your models here.

from .models import Goods
from .models import GroupGoods
from .models import Manufacturer
from .models import Country
from .models import InShop
from .models import Invoice
from .models import Bill

class BillAdmin(admin.ModelAdmin):
    fields = ['goodID', 'goodcount',  'goodPrice', 'ClientID']

admin.site.register(Bill, BillAdmin)

admin.site.register(Goods)
admin.site.register(GroupGoods)
admin.site.register(Manufacturer)
admin.site.register(Country)
admin.site.register(InShop)
admin.site.register(Invoice)
