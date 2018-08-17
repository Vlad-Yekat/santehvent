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

class InShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'goodcount', 'goodreserv', 'goodPrice')
    list_filter = ['goodreserv']
    search_fields = ['goodid']

    fieldsets = [
        (None, {'fields': ['goodID']}),
        ('in stock inform', {'fields': ['goodcount','goodreserv','goodPrice']})
    ]


admin.site.register(InShop, InShopAdmin)

admin.site.register(Goods)
admin.site.register(GroupGoods)
admin.site.register(Manufacturer)
admin.site.register(Country)
admin.site.register(Invoice)
