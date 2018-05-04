from django.contrib import admin

# Register your models here.

from .models import good, group

admin.site.register(good)
admin.site.register(group)